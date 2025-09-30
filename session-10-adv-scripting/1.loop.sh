#!/bin/bash

for i in {1..5}
do
   echo "number $i"
done

echo "Another way to iterate through numbers"
for i in $(seq 5 10)
do
   echo "number $i"
done

#while loop
count=1
while [ $count -le 5 ]
do
   echo "count is $count"
   ((count++))
done

##until loop
num=1
until [ $num -gt 5 ]
do
   echo "num $num"
   ((num++))
done

## Loops through files

for file in *.txt
do
   echo "Processing $file"
done