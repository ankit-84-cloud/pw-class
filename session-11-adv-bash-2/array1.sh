# Array operations 
nums=(1 2 3 4 5 )
echo "${nums[@]}"        # prints all elements
#append elements
nums+=(6)
echo "${nums[@]}"        # prints all elements

#append multiple elements
nums+=(7 8 9 10)
echo "${nums[@]}"        # prints all elements
#insert element at specific index between 3 to 5
nums[3]=20
echo "after insert ${nums[@]}"       #replaces 4 with 20
nums[11]=90
echo "after append ${nums[@]}"      # adds 90 at index 11

#delete element at specific index
unset 'nums[11]'

echo "after delete ${nums[@]}"      # removes 90