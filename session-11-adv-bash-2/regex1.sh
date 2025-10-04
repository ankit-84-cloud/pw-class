#!/bin/bash

read -rp "enter somthing: " data
if [[ $data =~ ^[0-9]+$ ]]; then
  echo "it's an integer number"
else
  echo "not an integer number"
fi

# -r prevents backslash (\) interpreted as an escape character
# -p prints and read input in variable named data

#=~ : is used for regex matching in bash
## [[....]] advanced bash test command
## more powerful than [....]