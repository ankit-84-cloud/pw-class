#!/bin/bash

num=10
if [ $num -gt 5 ]; then
   echo "$num is greater than 5"
else
   echo "$num is less than or equal to 5"
fi

name="John"
if [ "$name" == "John" ]; then
   echo "Hello, John!"
else
   echo "You are not John."
fi

#Logical operators
age=17
if [ $age -ge 18 ] && [ $age -le 30 ]; then
   echo "You are eligible for the youth program."
else
   echo "You are not eligible for the youth program."
fi
user="ankit"
if [ "$user" == "admin" ] || [ "$user" == "root" ]; then
   echo "You have administrative privileges."
else
   echo "You do not have administrative privileges."
fi