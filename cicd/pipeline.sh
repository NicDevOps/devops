#!/bin/bash
#
#

source ~/projects/project-name/cicd/functions.sh

echo -e "$GREEN######################################################################################$END"
echo -e "$GREEN#                             RUNNING PIPELINE                                       #$END"
echo -e "$GREEN######################################################################################$END"

BUILD_SCRIPT_PATH="~/projects/project-name/cicd/build.sh"
RUN_SCRIPT_PATH="~/projects/project-name/cicd/run.sh"
RUN_ASCII_ART_PATH="~/projects/project-name/apps/ascii_app/app.py"

bash -c "$BUILD_SCRIPT_PATH"
bash -c "$RUN_SCRIPT_PATH"
bash -c "python3 $RUN_ASCII_ART_PATH"

#ansible-playbook -i ~/projects/project-name/ansible/inventory.yaml ~/projects/project-name/ansible/main.yaml


