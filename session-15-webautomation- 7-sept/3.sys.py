import sys  

print("python version", sys.version)
print("python Executable",sys.executable)
print("system Platform", sys.platform)
#print("module Search path", sys.path)

print("file name", sys.argv[0])

#exit program
#sys.exit(0)

sys.stderr.write("this is Standard error")