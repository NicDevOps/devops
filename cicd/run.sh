#!/bin/bash

source ~/projects/devops/cicd/functions.sh

echo -e "$BLUE######################################################################################$END"
echo -e "$BLUE#                                 RUN STAGE                                          #$END"
echo -e "$BLUE######################################################################################$END"
echo
echo
echo -e "                                         _-----o----_"
echo -e "                                /|__/|  /            |"
echo -e "                                |_  _/ /              |"
echo -e "                                  | |_|          () __|"
echo -e "                                   |                |_"
echo -e "                                    |     %__%       /"
echo -e "$BLUE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$END"

~/projects/devops/apps/rpi-discord/run.sh

