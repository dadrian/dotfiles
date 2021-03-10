# OS X, default to 8
if [ -x /usr/libexec/java_home ]; then
  unset JAVA_HOME
  if /usr/libexec/java_home -v 1.8 > /dev/null 2>&1; then
    export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
  else
    export JAVA_HOME=$(/usr/libexec/java_home)
  fi
fi

if [ -x "$HOME/Library/Android/sdk" ]; then
  export ANDROID_HOME="$HOME/Library/Android/sdk"
  export PATH="$PATH:$ANDROID_HOME/platform-tools"
fi
