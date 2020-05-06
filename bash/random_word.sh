#!/bin/bash

# Using random numbers

word=$1

newword="$word-$RANDOM"
echo "$newword"