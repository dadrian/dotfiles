# Virtualenv
export PIP_RESPECT_VIRTUALENV=true
export VIRTUALENV_DISTRIBUTE=true

# Virtualenv Wrapper
if [ -f $VIRTUALENV_WRAPPER_BIN ]; then
  export WORKON_HOME="${HOME}/.virtualenvs"
  export PROJECT_HOME="${HOME}/src"
  source $VIRTUALENV_WRAPPER_BIN
fi
