#!/bin/bash



ssh pi@rpi 'git -C /home/pi/projects/devops checkout -f'

ssh pi@rpi 'cd /home/pi/projects/devops/apps/rpi-discord; docker-compose build'
