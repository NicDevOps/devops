#!/bin/bash

# Comparing strings and using if statement

echo "give two strings to compare"

read str1 str2

if [ "$str1" = "$str2" ] ; then
    echo "The first string: $str1, is the same as the second string: $str2"
else
    echo "The first string: $str1, is not the same as the second string: $str2"

fi