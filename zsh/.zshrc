export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin
export INCLUDE_PATH=/usr/local/include:/usr/include

if [ -d "/opt/homebrew/bin" ]; then
  export PATH="/opt/homebrew/bin:$PATH"
fi

if [ -d "/usr/local/go/bin" ]; then
  export PATH="/usr/local/go/bin:$PATH"
fi


# starship
function config_starship {
  config_ls_colors
  if ! command -v starship &>/dev/null; then
    echo >&2 "Missing starship!"
  else
    eval "$(starship init zsh)"
  fi
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
  if [ -f $HOME/.oh-my-zsh/oh-my-zsh.sh ]; then
    export ZSH="$HOME/.oh-my-zsh"
    ZSH_THEME="robbyrussell"
    plugins=(git)
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
bindkey '[A' history-beginning-search-backward
bindkey '[B' history-beginning-search-forward
#bindkey '^R' history-incremental-search-backward

# Set up constants
source $HOME/.dotfiles/_const.sh

# Load everything else
source $HOME/.dotfiles/term.sh
source $HOME/.dotfiles/editor.sh
source $HOME/.dotfiles/fly.sh
source $HOME/.dotfiles/gcloud.sh
source $HOME/.dotfiles/golang.sh
source $HOME/.dotfiles/java.sh
source $HOME/.dotfiles/python.sh
source $HOME/.dotfiles/mactex.sh
source $HOME/.dotfiles/rust.sh
source $HOME/.dotfiles/ssh.sh
source $HOME/.dotfiles/ssl-osx.sh
source $HOME/.dotfiles/zig.sh

# Only load extras if it exists
if [ -f .dotfiles/extras.sh ]; then
  source $HOME/.dotfiles/extras.sh
fi

# Force $HOME binaries to the top of $PATH
export PATH=$HOME/bin:$HOME/.bin:$PATH

if (( ${+DADRIAN_STARSHIP} )); then
  config_starship
fi
