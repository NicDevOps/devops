#!/bin/bash

echo "Enter filename"

read name

# -x Check if file is executable

if [ -x $name ] ; then
    echo "The file is executable"
else
    echo "The file is not executable"
fi

