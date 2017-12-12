#!/bin/bash

set -e -x

yum -y update && yum clean all
yum -y install epel-release && yum clean all
yum -y install python-pip && yum clean all
pushd helloworld/docker
  pip install --trusted-host pypi.python.org -r requirements.txt
  python helloworld_tests.py
popd
