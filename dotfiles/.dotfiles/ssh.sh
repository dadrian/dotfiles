if [ -z ${SSH_AUTH_SOCK+x} ]; then
  if [ $(uname -s) = "Linux" ]; then
    export SSH_AUTH_SOCK=$XDG_RUNTIME_DIR/ssh-agent.socket
  fi
fi
