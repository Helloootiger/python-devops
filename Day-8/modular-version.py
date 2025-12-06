# Convert string to list and get the variables using input, expectional handling in modular approach

import os

def list_files_in_folder(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"

def main():
    folder_path = input("Please provide folder name:").split()

    for folder in folder_path:
        files, error_message = list_files_in_folder(folder)
        if files:
            print("Files in:", folder)
            for file in files:
                print(file)
            
        else:
            print("Error in:", folder , error_message)
    

if __name__ == "__main__":
    main()




