.PHONY: default
default: help

.PHONY: dependencies
dependencies:  ## Install dependencies for this script
	@command -v stow >/dev/null 2>&1 || brew install stow 2>/dev/null || sudo apt-get install -y stow 2>/dev/null || sudo yum install -y stow 2>/dev/null || { echo >&2 "Please install GNU stow"; exit 1; }

.PHONY: check-dependencies
check-dependencies:
	@command -v stow >/dev/null 2>&1 || { echo >&2 "Missing GNU stow"; exit 1; }

STOWABLE := alacritty dotfiles git ssh tmux zsh
.PHONY: $(STOWABLE)
$(STOWABLE):
	stow -t $$HOME -d $(shell pwd) $(STOW_ARGS) $@

$$HOME/.config:
	mkdir -p $@

STOWABLE_DOT_CONFIG := starship
.PHONY: $(STOWABLE_DOT_CONFIG)
$(STOWABLE_DOT_CONFIG): | $$HOME/.config
	stow -t $$HOME/.config -d $(shell pwd) $(STOW_ARGS) $@

.PHONY: stow
stow: $(STOWABLE) $(STOWABLE_DOT_CONFIG)

.PHONY: unstow
unstow: STOW_ARGS += -D
unstow: $(STOWABLE) $(STOWABLE_DOT_CONFIG)

.PHONY: vscode
vscode: | $$HOME/.config
	./vscode/install.sh
	cat ./vscode/extensions/extensions.txt | xargs -n1 code --install-extension

.PHONY: unvscode
unvscode:
	if [ $(VSCODE_SETTINGS) -ef $$(pwd)/vscode/user/settings.json ]; then rm $(VSCODE_SETTINGS); echo '{}' > $(VSCODE_SETTINGS); fi

.PHONY: link-bin
link-bin:
	ln -sni $$(pwd)/bin $$HOME/.bin

.PHONY: unlink-bin
unlink-bin:
	if [ $$HOME/.bin -ef $$(pwd)/bin ]; then rm $$HOME/.bin; fi

install: check-dependencies stow link-bin vscode ## Install dotfiles
uninstall: unvscode unlink-bin unstow ## Uninstall dotfiles

.PHONY: osx
osx: ## Install OS X specific-things (not undoable)
	brew bundle install --file=osx/Brewfile
	cp osx/osx-ssh ssh/.ssh/config.d
	defaults write com.microsoft.VSCode ApplePressAndHoldEnabled -bool false

.PHONY: linux
linux: ## Install Linux-specific things
	@echo 'Done'

.PHONY: help
help: ## List tasks with documentation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' "$(firstword $(MAKEFILE_LIST))" | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
