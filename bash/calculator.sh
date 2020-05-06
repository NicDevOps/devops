#!/bin/bash

# Calculator 

# Input numbers and operator

echo "Enter a number"
read num1

echo "Enter a second number"
read num2

echo "Choose an operator a (add), s (sub), m (mult) or d (div)"
read op

# Functions

add() {
    answer=$(($num1 + $num2))
}

sub() {
    answer=$(($num1 - $num2))
}

mult() {
    answer=$(($num1 * $num2))
}

div() {
    answer=$(($num1 / $num2))
}

# Working functions

if [[ $op == a ]] ; then add $num1 $num2
elif [[ $op == s ]] ; then sub $num1 $num2
elif [[ $op == m ]] ; then mult $num1 $num2
elif [[ $op == d ]] ; then div $num1 $num2
else
echo "$op is not a, s, m or d, aborting ; exit 2"
fi

# Displaying answser

echo "$num1 $op $num2"  
echo Awnser is $answer