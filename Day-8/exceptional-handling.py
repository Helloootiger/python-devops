# Convert string to list and get the variables using input, expectional handling

import os

folder_path = input("please provide the folder name:").split()  

for folder in folder_path:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please give valid folder name, given folder not exist:" + folder)
        break

    for file in files:
        print(file)