#!/bin/bash
#
#

source ~/projects/devops/cicd/functions.sh

echo -e "$GREEN######################################################################################$END"
echo -e "$GREEN#                             RUNNING PIPELINE                                       #$END"
echo -e "$GREEN######################################################################################$END"

BUILD_SCRIPT_PATH="~/projects/devops/cicd/build.sh"
RUN_SCRIPT_PATH="~/projects/devops/cicd/run.sh"
RUN_ASCII_ART_PATH="~/projects/devops/apps/ascii_app/app.py"

bash -c "$BUILD_SCRIPT_PATH"
bash -c "$RUN_SCRIPT_PATH"
bash -c "python3 $RUN_ASCII_ART_PATH"

#ansible-playbook -i ~/projects/devops/ansible/inventory.yaml ~/projects/devops/ansible/main.yaml


