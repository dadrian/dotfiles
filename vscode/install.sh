UNAME_S=$(uname -s)
if [ $UNAME_S = "Linux" ]; then
  VSCODE_SETTINGS=$HOME/.config/Code/User
  mkdir -p $VSCODE_SETTINGS
  ln -sni $(pwd)/vscode/user/settings.json $VSCODE_SETTINGS/settings.json
elif [ $UNAME_S = "Darwin" ]; then
  set -x
  mkdir -p $HOME/Library/Application\ Support/Code/User
  ln -sni $(pwd)/vscode/user/settings.json $HOME/Library/Application\ Support/Code/User/settings.json
fi
