#!/bin/bash

# Example of testing numbers using argument to compare them with various operators

#AGE=$1

echo "Enter your age"

read AGE

if [[ $AGE -ge 20 ]] && [[ $AGE -lt 30 ]] ; then
    echo "You are in your 20s"
elif [[ $AGE -ge 30 ]] && [[ $AGE -lt 40 ]] ; then
    echo "You are in your 30s"
elif [[ $AGE -ge 40 ]] && [[ $AGE -lt 50 ]] ; then
    echo "You are in your 40s"
else 
    echo "At $AGE, you are not in the proper range of 20-49"
fi
