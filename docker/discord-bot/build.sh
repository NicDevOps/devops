#!/bin/bash

docker images -a

docker rmi -f $(docker images -a -q)

docker build -t orion:5000/discord-bot ~/projects/project-name/docker/discord-bot

