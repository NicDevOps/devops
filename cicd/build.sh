#!/bin/bash

source ~/projects/devops/cicd/functions.sh

echo -e "$MAGENTA######################################################################################$END"
echo -e "$MAGENTA#                                  BUILD STAGE                                       #$END"
echo -e "$MAGENTA######################################################################################$END"

~/projects/devops/apps/rpi/build.sh

