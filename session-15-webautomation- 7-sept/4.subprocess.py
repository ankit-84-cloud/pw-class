import subprocess

subprocess.run(["echo","hello from subprocess"])

#run command in shell 

result=subprocess.run(["ls", "-1"],capture_output=True,text=True)
print("STDOut:",result.stdout)
print("STDErr:",result.stderr)
