#!/bin/bash

docker images -a

docker rmi -f $(docker images -a -q)

docker build -t nick/app1 ~/projects/project-name/docker/app1

