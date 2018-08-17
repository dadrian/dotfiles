#!/usr/bin/env bash
set -e

mkdir -p $HOME/.bin
CLOUD_SQL_INSTALL_PATH="$HOME/.bin/cloud_sql_proxy"
curl -o $CLOUD_SQL_INSTALL_PATH https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64
chmod a+x $CLOUD_SQL_INSTALL_PATH

