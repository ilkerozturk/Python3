import os

print(os.name)  # Operating system name 
print(os.getcwd())  # Current working directory
print(os.listdir())  # List of files and directories in the current directory
print(os.path.abspath("15.2_os-metodu.py"))  # Absolute path of the
print(os.path.exists("15.2_os-metodu.py"))  # Check if the file exists
print(os.path.isfile("15.2_os-metodu.py"))  # Check if it's a file
print(os.path.isdir("some_directory"))  # Check if it's a directory
print(os.path.getsize("15.2_os-metodu.py"))  # Size of the file in bytes
print(os.path.splitext("15.2_os-metodu.py"))  # Split file name and extension