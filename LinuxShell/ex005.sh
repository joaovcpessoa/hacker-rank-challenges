#!/bin/bash

echo "Write x:"
read x
echo "Write y:"
read y

sum=$((x + y))
difference=$((x - y))
product=$((x * y))
quotient=$((x / y))

echo "Sum: $sum"
echo "Difference: $difference"
echo "Product: $product"
echo "Quotient: $quotient"