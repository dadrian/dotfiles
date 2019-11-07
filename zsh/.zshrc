export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin

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
source $HOME/.dotfiles/_const.sh

# Load everything else
source $HOME/.dotfiles/gcloud.sh
source $HOME/.dotfiles/golang.sh
source $HOME/.dotfiles/python.sh
source $HOME/.dotfiles/mactex.sh
source $HOME/.dotfiles/rust.sh
source $HOME/.dotfiles/travis.sh
source $HOME/.dotfiles/z.sh

# Only load extras if it exists
if [ -f .dotfiles/extras.sh ]; then
  source $HOME/.dotfiles/extras.sh
fi

# Force $HOME binaries to the top of $PATH
export PATH=$HOME/bin:$HOME/.bin::$PATH
