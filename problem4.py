import os

# Specify the directory path
directory_path = '/'  # You can change this to any directory you want

# Get the list of files and directories in the specified directory
try:
    contents = os.listdir(directory_path)

    print(f"Contents of the directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access the directory '{directory_path}'.")
