#!/bin/bash

# True false checker script

echo "Run program [y or Y]"

read a

if [ $a == "y" ] || [ $a == "Y" ]
then 
  echo "yes"
else
  echo "no"  
fi
