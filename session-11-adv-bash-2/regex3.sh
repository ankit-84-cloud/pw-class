read -rp "enter an text: " email
if [[ $email =~ ^ab*c$ ]]; then
  echo "valid text"
else
  echo "not a valid text"
fi

#correct patterns

#ac
#abc
#abbc
#abbbc
#abbbbc
#incorrect patterns
#abba   #aabbc #aabbbaac
