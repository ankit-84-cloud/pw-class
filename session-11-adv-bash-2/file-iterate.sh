for file in $(ls *.*); do   
  echo "Processing $file"
done

for line in $(cat array.sh); do
  echo "Line: $line"
done