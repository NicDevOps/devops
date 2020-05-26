#!/bin/bash

echo 'running rpi app..'

#scp ~/projects/devops/apps/rpi/test123.py pi@rpi:~/projects/rpi

ssh pi@rpi 'GIT_WORK_TREE=/home/pi/projects/devops git checkout -f'

echo 'works!'
