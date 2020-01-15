if [ $(uname -s) = "Darwin" ]; then
    (echo $LIBRARY_PATH | grep '/usr/local/opt/openssl@1.1/lib/') || export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl@1.1/lib/
fi
