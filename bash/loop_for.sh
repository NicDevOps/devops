#!/bin/bash

sum=0

echo "Enter a number"

read num1

echo "Enter a second number"

read num2

for j in $num1 $num2
do
    sum=$(( $sum + $j ))
done

echo "The sum is: $sum"