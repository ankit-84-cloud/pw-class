import sys

print("Script name:", sys.argv[0])  # script name
print("Arguments:", sys.argv[1:])  # arguments passed to script

#command to execute: 
#py 03cmdarg.py file.txt file2.txt file3.txt hello ankit

# iterate using for loop
for i in sys.argv[1:]:
    print(i)
    print("Argument:", i)


