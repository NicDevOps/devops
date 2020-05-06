#!/bin/bash

# Part of a string

#NAME=Eddie.Haskel

#first=${NAME:0:5}

#echo "first name = $first"

##################################

NAME=Eddie.Haskel

last=${NAME#*.}

echo "last name = $last"