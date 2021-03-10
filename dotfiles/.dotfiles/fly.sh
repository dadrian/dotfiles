if [ -z ${FLY_INSTALL+x} ]; then
  # Check common install locations
  if [ -x "$HOME/.fly" ]; then
    export FLY_INSTALL="$HOME/.fly"
  fi
fi

# Fly is installed, add it to path
if [ ! -z ${FLY_INSTALL+x} ]; then
  export PATH="$PATH:$FLY_INSTALL/bin"
fi
