#!/bin/bash 

set -e -x

yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2

yum-config-manager \
  --add-repo \
  https://download.docker.com/linux/centos/docker-ce.repo

yum install -y docker-ce
systemctl start docker

curl \
  -L https://github.com/aelsabbahy/goss/releases/download/_VERSION_/goss-linux-amd64 \
  -o /usr/local/bin/goss

chmod +rx /usr/local/bin/goss
curl \
  -L https://raw.githubusercontent.com/aelsabbahy/goss/_VERSION_/extras/dgoss/dgoss \
  -o /usr/local/bin/dgoss

chmod +rx /usr/local/bin/dgoss

pushd helloworld/docker
  /usr/local/bin/dgoss run -p 8080:8080 helloworld
popd
