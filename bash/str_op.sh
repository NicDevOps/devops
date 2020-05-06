#!/bin/bash

# Check two string arguments were given

[[ $# -lt 2 ]] && \
    echo "Usage: Give two strings as arguments" && exit 1

str1=$1
str2=$2

#-----------------------------------------------
## Test command

echo "Is string 1 zero length? Value of 1 means FALSE"
[ -z "$str1" ]
echo $?

# Note if $str1 is empty, the test [ -z $str1 ] would fail
#                             but [[ -z $str1 ]] succeeds
# i.e., with [[ ]] it works even without the quotes

# Comparing the length of two strings

len1=${#str1}
len2=${#str2}
echo "length of string1 = $len1, length of string2 = $len2"

if [ $len1 -gt $len2 ]
then
    echo "String  1 is longer then string 2"
else
    if [ $len2 -gt $len1 ]
    then
        echo "String 2 is longer then string 1"
    else
        echo "String 1 is the same length as string 2"
    fi
fi

# Compare the two strings to see if are the same

if [[ $str1 == $str2 ]]
then
    echo "String 1 is the same as string 2"
else
    if [[ $str1 != $str2 ]]
    then
        echo "String 1 is not the same as string 2"
    fi
fi            