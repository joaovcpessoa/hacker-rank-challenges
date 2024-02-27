#!/bin/bash

echo "Write x:"
read x
echo "Write y:"
read y
echo "Write z:"
read z

if [ "$x" -eq "$y" ] && [ "$y" -eq "$z" ]; then
    echo "EQUILATERAL"
elif [ "$x" -eq "$y" ] || [ "$x" -eq "$z" ] || [ "$y" -eq "$z" ]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi