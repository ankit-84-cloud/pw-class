import os
import platform

current_directory = os.getcwd()
print(f"Current working Directory: {current_directory}")

print(f"CPU Count: {os.cpu_count()}")
print(f"CURRENT DIR: {os.getcwd()}")

print(f"Architecture : {platform.architecture()}")
print(f"Python Version: {platform.python_version()}")
