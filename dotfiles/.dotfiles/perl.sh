
if [ -x "$HOME/perl5" ]; then
  export PERL_HOME="$HOME/perl5";
  export PATH="$HOME/perl5:$PATH";
  export PERL5LIB="$PERL_HOME/lib/perl5";
  export PERL_MB_OPT="--install_base \"$PERL_HOME\"";
  export PERL_LOCAL_LIB_ROOT="$PERL_HOME";
  export PERL_MM_OPT="INSTALL_BASE=$PERL_HOME";
fi
