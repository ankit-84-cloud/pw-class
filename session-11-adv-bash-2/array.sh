# Array declaration
names=("alex" "john" "mike" "devid" "bob")

#Accessing array elements
echo "First element: ${names[0]}"
echo "Second element: ${names[1]}"
echo "Third element: ${names[2]}"
echo "All elements: ${names[@]}"
echo "Total elements: ${#names[@]}"

#Accessing length of a specific element
echo "Length of first element: ${#names[0]}"
echo "Length of second element: ${#names[1]}"
echo "Length of third element: ${#names[2]}"

#change Array elements
names[1]="john sam"
echo "After changing second element: ${names[1]}"

#print all elements using loop
for name in "${names[@]}"; do
  echo "Name: $name"
done    

# print them in one line
result=""
for name in "${names[@]}"; do
  result+="$name "
done
echo "All names in one line: $result"

echo "${result%, }"  # Remove last space