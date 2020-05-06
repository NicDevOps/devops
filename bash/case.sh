#!/bin/bash

echo "Enter a month in numerical value between 1 - 12"
read month

case "$month" in
    "1")    echo "janvier";;
    "2")    echo "fevrier";;
    "3")    echo "mars";;
    "4")    echo "avril";;
    "5")    echo "mai";;
    "6")    echo "juin";;
    "7")    echo "juillet";;
    "8")    echo "aout";;
    "9")    echo "septembre";;
    "10")   echo "octobre";;
    "11")   echo "novembre";;
    "12")   echo "december";;
    *)      echo "This is not a month" && exit 1;;
esac