#!/bin/bash
my_name="Kashyap"
echo "Hello, $my_name!"
echo "Welcome to DevOps, $my_name!"
echo "This is a sample script, $my_name."
mkdir "$my_name"_dir
cd "$my_name"_dir || exit
touch file1.txt file2.txt file3.txt
echo "enter your age"
read age
echo "Your age is $age"

## Arthmetic operations
num1=10
num2=20
sum=$((num1 + num2))
echo "The sum of $num1 and $num2 is: $sum"

#sample comment
username="Ankit kashyap"
today_date=$(date +%Y-%m-%d-%H:%M:%S)
echo "Hello, $username! Today's date is $today_date."