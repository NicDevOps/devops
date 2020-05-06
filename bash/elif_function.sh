#!/bin/bash

# This script checks if you are a Beatle 

echo "Give your name"

read name

if [ "$name" == John ] ; then
    echo "Hello $name"
elif [ "$name" == Ringo ] ; then
    echo "Hello $name"
elif [ "$name" == Paul ] || [ "$name" == George ] ; then
    echo "Hello $name"
else 
    echo "Forget it $name, You are not a Beatle"
fi
