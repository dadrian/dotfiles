function update_alacritty_terminfo {
    ALACRITTY_VERSION=$(alacritty --version | cut -d ' ' -f 2)
    F=$(mktemp)
    TERMINFO_URL="https://raw.githubusercontent.com/alacritty/alacritty/v$ALACRITTY_VERSION/extra/alacritty.info"
    curl -s $TERMINFO_URL > $F || echo "unable to fetch terminfo from $TERMINFO_URL"
    tic -xe alacritty,alacritty-direct $F
    echo 'updated, restart alacritty for changes to take effect'
}

function update_tmux_terminfo {
  F=$(mktemp)
  curl -sL https://invisible-island.net/datafiles/current/terminfo.src.gz > $F
  gunzip -cd $F > $F.src
  echo "fetched a terminfo from the internet to $F.src"
  if read -q "REPLY?install?"; then
    tic -xe tmux-256color $F.src
    echo 'updated, restart tmux server for changes to take effect'
  else
    echo ''
    echo 'aborted'
    return 1
  fi
}

if type "alacritty" > /dev/null ; then
  if infocmp alacritty > /dev/null 2>&1 ; then
    # Already installed terminfo
  else
    echo 'missing alacritty terminfo, run "update_alacritty_terminfo"'
  fi
fi

if infocmp tmux-256color > /dev/null 2>&1 ; then
  # Already have tmux-256color
else
  echo 'missing tmux-256color terminfo, run "update_tmux_terminfo"'
fi
