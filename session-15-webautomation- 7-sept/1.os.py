import cmd
import os

print(os.listdir())
cwd=os.getcwd()
print("current Working directory: ",cwd)

#create new directory
new_dir="demo_folder"
if not os.path.exists(new_dir):
  os.mkdir(new_dir)
  print(f"Created directory: {new_dir}")


  #Rename Directory
  rename_dir="rename_folder"
  if not os.path.exists("rename_folder"):
    os.rename(new_dir,"rename_folder")
    print(f"Rename{new_dir} to {rename_dir}")

#Remove
#os.rmdir(rename_dir)
#print(f"Removed {rename_dir}")