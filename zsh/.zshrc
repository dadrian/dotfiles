export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin
export INCLUDE_PATH=/usr/local/include:/usr/include

# starship
function config_starship {
  config_ls_colors
  eval "$(starship init zsh)"
}

function config_ls_colors {
  # Steal color configuration from oh-my-zsh if using Starship
  export LSCOLORS="Gxfxcxdxbxegedabagacad"
  if command diff --color . . &>/dev/null; then
    alias diff='diff --color'
  fi
  if [[ "$OSTYPE" == (darwin|freebsd)* ]]; then
    # this is a good alias, it works by default just using $LSCOLORS
    ls -G . &>/dev/null && alias ls='ls -G'
    ls --color -d . &>/dev/null && alias ls='ls --color=tty' || { ls -G . &>/dev/null && alias ls='ls -G' }

    # Take advantage of $LS_COLORS for completion as well.
    zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
  fi
}

# oh-my-zsh
function config_oh_my_zsh {
  export ZSH="$HOME/.oh-my-zsh"
  ZSH_THEME="robbyrussell"
  plugins=(git)
  if [ -f $ZSH/oh-my-zsh.sh ]; then
    source $ZSH/oh-my-zsh.sh
  else
    echo "Missing oh-my-zsh!"
  fi
}

DADRIAN_STARSHIP=1
if (( ${+DADRIAN_STARSHIP} )); then
  # Configuration has to happen at the end
else
  config_oh_my_zsh
fi

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
bindkey '^R' history-incremental-search-backward

# Set up constants
source $HOME/.dotfiles/_const.sh

# Load everything else
source $HOME/.dotfiles/editor.sh
source $HOME/.dotfiles/gcloud.sh
source $HOME/.dotfiles/golang.sh
source $HOME/.dotfiles/java.sh
source $HOME/.dotfiles/python.sh
source $HOME/.dotfiles/mactex.sh
source $HOME/.dotfiles/rust.sh
source $HOME/.dotfiles/ssl-osx.sh
source $HOME/.dotfiles/travis.sh
source $HOME/.dotfiles/z.sh

# Only load extras if it exists
if [ -f .dotfiles/extras.sh ]; then
  source $HOME/.dotfiles/extras.sh
fi

# Force $HOME binaries to the top of $PATH
export PATH=$HOME/bin:$HOME/.bin:$PATH

if (( ${+DADRIAN_STARSHIP} )); then
  config_starship
fi

