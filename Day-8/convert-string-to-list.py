#  Convert string to list and get the variables using input

#folder = input("please provide the folder name:")
#print(folder)


# separating the string
#folder = input("please provide the folder name:").split()
#print(folder)


# for loop for each folder

#folder_path = input("please provide the folder name:").split()

#for folder in folder_path:
#    print(folder)

# to list files in folder

import os

folder_path = input("please provide the folder name:").split()  

for folder in folder_path:
    files = os.listdir(folder)

    for file in files:
        print(file)
