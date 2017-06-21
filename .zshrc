# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH=$HOME/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

# oh-my-zsh
export ZSH="/Users/$USER/.oh-my-zsh"
ZSH_THEME="robbyrussell"
plugins=(git)
source $ZSH/oh-my-zsh.sh


# Base Shell Configuration
export LANG=en_US.UTF-8
export EDITOR='vim'
set -o vi
DADRIAN_SHELL_NAME=$(basename $SHELL)

# Remove oppressive open file limits
ulimit -n 8192

# Better up arrow behavior
bindkey 'OA' history-beginning-search-backward
bindkey 'OB' history-beginning-search-forward

# Set up constants
source .dotfiles/_const.sh

# Load everything else
source .dotfiles/gcloud.sh
source .dotfiles/golang.sh
source .dotfiles/python.sh
source .dotfiles/mactex.sh
source .dotfiles/rust.sh
source .dotfiles/z.sh

# Only load extras if it exists
if [ -f .dotfiles/extras.sh ]; then
  source .dotfiles/extras.sh
fi
