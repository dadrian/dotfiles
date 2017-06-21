.PHONY: all clean dotfiles ssh vim

all: dotfiles ssh vim

dotfiles:
	ln -sfn $(CURDIR)/.zshrc $(HOME)/.zshrc
	ln -sfn $(CURDIR)/.dotfiles $(HOME)/.dotfiles

ssh:
	if [ -d $(CURDIR)/.ssh ]; then ln -sfn $(CURDIR)/.ssh $(HOME)/.ssh; fi

vim:
	if [ -d $(CURDIR)/.vim ]; then ln -sfn $(CURDIR)/.vim $(HOME)/.vim; fi

clean:
	rm -f $(HOME)/.zshrc
	rm -f $(HOME)/.dotfiles
	rm -f $(HOME)/.ssh
	rm -f $(HOME)/.vim
