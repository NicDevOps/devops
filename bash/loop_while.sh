#!/bin/bash

# echo "Want to continue ? [y|n]"
# read ans

##Debug mode set -x
# if [ $num1 != "" ] 
# then
#     set -x
# fi
    
# While is true execute command again. Until is false execute command again

# while [ $num1 -gt 1 ]
# do
#     echo "The number $num1 is greater than one"
#     num1=$(( $num1 - 1 ))
# done
# exit 0

ans="y"

while [ $ans == "y" ]
do
    echo "Enter a number"
    read num
    echo "$(( $num * 2 ))"

    echo "Want to continue ? [y|n]"
    read ans
done
exit 0