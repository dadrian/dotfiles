.PHONY: all clean dotfiles git ssh vim slack-term

all: dotfiles ssh vim git

dotfiles:
	ln -sfn $(CURDIR)/.zshrc $(HOME)/.zshrc
	ln -sfn $(CURDIR)/.dotfiles $(HOME)/.dotfiles

git:
	if [ -d $(CURDIR)/git ]; then ln -sfn $(CURDIR)/git $(HOME)/.git; ln -sfn $(HOME)/.git/gitconfig $(HOME)/.gitconfig; fi

ssh:
	if [ -d $(CURDIR)/ssh ]; then ln -sfn $(CURDIR)/ssh $(HOME)/.ssh; fi

vim:
	if [ -d $(CURDIR)/vim ]; then ln -sfn $(CURDIR)/vim $(HOME)/.vim; fi

clean:
	rm -f $(HOME)/.zshrc
	rm -f $(HOME)/.dotfiles
	rm -f $(HOME)/.git
	rm -f $(HOME)/.ssh
	rm -f $(HOME)/.vim
