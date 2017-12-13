#!/bin/bash 

set -e -x

yum update -y && yum clean all
yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2

yum-config-manager \
  --add-repo \
  https://download.docker.com/linux/centos/docker-ce.repo

yum install -y docker-ce

curl \
  -L https://github.com/aelsabbahy/goss/releases/download/v0.3.5/goss-linux-amd64 \
  -o /usr/local/bin/goss

chmod +rx /usr/local/bin/goss
curl \
  -L https://raw.githubusercontent.com/aelsabbahy/goss/master/extras/dgoss/dgoss \
  -o /usr/local/bin/dgoss
chmod +rx /usr/local/bin/dgoss

PATH=$PATH:/usr/local/bin
pushd helloworld/docker
  dgoss run -d -p 8080:8080 agoehring/helloworld
popd
