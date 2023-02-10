# Let's leave this disabled for a bit and see if we need it any more.
#
# if [ $(uname -s) = "Darwin" ]; then
#   if [ -d "/usr/local/opt/openssl@1.1/lib" ]; then
#     (echo $LIBRARY_PATH | grep '/usr/local/opt/openssl@1.1/lib/' > /dev/null) || export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl@1.1/lib/:/usr/local/lib
#   fi
# fi
