read -rp "enter an email: " email
if [[ $email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
  echo "valid email"
else
  echo "not a valid email"
fi

## 5min task ##
#write a code to take ip from user
# write regex to validate ip address
## if match pattern print connected
## else print incorrect ip address

#!/bin/bash
read -rp "enter an ip address: " ip
if [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "connected"
else
  echo "incorrect ip address"
fi

# match exactly 8 digits in a row with simaple regex
#pattern [0-9]{8}
#pattern ^[0-9]{8}$
