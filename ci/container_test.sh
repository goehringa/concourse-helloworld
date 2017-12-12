#!/bin/bash 

set -e -x

curl \
  -L https://github.com/aelsabbahy/goss/releases/download/_VERSION_/goss-linux-amd64 \
  -o /usr/local/bin/goss
chmod +rx /usr/local/bin/goss
curl \
  -L https://raw.githubusercontent.com/aelsabbahy/goss/_VERSION_/extras/dgoss/dgoss \
  -o /usr/local/bin/dgoss
chmod +rx /usr/local/bin/dgoss

pushd helloworld/docker
  dgoss run -p 8080:8080 helloworld
popd
