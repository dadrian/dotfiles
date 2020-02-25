if type /usr/local/bin/vim > /dev/null 2>&1; then
  alias vi='/usr/local/bin/vim'
  export EDITOR="vim"
fi
if type nvim > /dev/null 2>&1; then
  alias vim='nvim'
  alias vi='nvim'
  export EDITOR="nvim"
fi
