#!/usr/bin/env bash
EXTENSIONS=("dadrian-colors")

for ext in ${EXTENSIONS[@]}; do
  pushd "extensions/$ext"
  npx vsce package
  mv *.vsix ../../vsix
  popd
done

