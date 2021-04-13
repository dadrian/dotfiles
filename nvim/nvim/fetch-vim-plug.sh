#!/usr/bin/env bash
mkdir -p $(dirname $0)/_cache
curl https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim > _cache/plug.vim
