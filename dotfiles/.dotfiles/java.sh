# OS X, default to 11
if [ -x /usr/libexec/java_home ]; then
  if /usr/libexec/java_home -v 11 > /dev/null 2>&1; then
    export JAVA_HOME=$(/usr/libexec/java_home -v 11)
  fi
fi
