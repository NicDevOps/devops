#!/bin/bash

source ~/projects/devops/cicd/functions.sh

echo -e "$RED######################################################################################$END"
echo -e "$RED#                                  BUILD: RPI-DISCORD                                #$END"
echo -e "$RED######################################################################################$END"

set -x

# ssh pi@rpi 'git -C /home/pi/projects/devops checkout -f'

# ssh pi@rpi 'cd /home/pi/projects/devops/apps/rpi-discord; docker-compose build'
