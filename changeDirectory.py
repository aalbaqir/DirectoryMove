import os
import shutil

def organize_files(source_directory, destination_directory):
    # Define file types and their corresponding destination folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.heic'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.zip','.pkg', '.md' ],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov']
    }

    # Ensure destination folders exist; create if not
    for folder in file_types.keys():
        folder_path = os.path.join(destination_directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Loop through files in the source directory
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue


        # Determine the file type based on the extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Move the file to the corresponding destination folder
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = os.path.join(destination_directory, folder)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print("Moved '" + filename + "' to '" + destination_folder + "'")

if __name__ == "__main__":
    # Specify the source and destination directories
    source_dir = '/Users/aidahalbaqir/Downloads'
    destination_dir = '/Users/aidahalbaqir/NewDownloads'

    # Call the function to organize files
    organize_files(source_dir, destination_dir)

    current_directory = os.getcwd()
print("Current Directory:", current_directory)
