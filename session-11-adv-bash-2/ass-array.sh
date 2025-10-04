declare -A capitals
capitals[India]="New Delhi"
capitals[France]="Paris"
capitals[Japan]="Tokyo"

#Accessing elements

echo "Capital of India: ${capitals[India]}"
echo "Capital of France: ${capitals[France]}"
echo "Capital of Japan: ${capitals[Japan]}"

## iterate
for capital in "${capitals[@]}"; do
  echo "$capital"
done

##iterate with keys and values both
for country in "${!capitals[@]}"; do
  echo "The capital of $country is ${capitals[$country]}"
done