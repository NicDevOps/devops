#!/bin/bash

source ~/projects/devops/cicd/functions.sh

echo -e "$RED######################################################################################$END"
echo -e "$RED#                                  RUN: RPI-SENSORS                                  #$END"
echo -e "$RED######################################################################################$END"

set -x

cd /home/git/projects/devops/apps/rpi-sensors

docker-compose --context rpi restart

# docker-compose --context rpi up -d

