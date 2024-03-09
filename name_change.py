import os
from os.path import isfile, join
import re

# Path to the directory containing folders of photos
path = '/Users/Buas/Desktop/Data Start/GitHub/Google-Image-Scraper/photos'

def extract_number(filename):
    match = re.search(r'_(\d+)', filename)
    if match:
        return int(match.group(1))
    return 0

# Change name
for foldername in sorted(os.listdir(path)):
    if not foldername.startswith('.'):  # Skip hidden files and directories
        folder_path = join(path, foldername)  # Full path to the folder
        count = 1  # Initialize counter for renaming files within this folder
        
        
        print("n files", len(os.listdir(folder_path)))
        for filename in sorted(os.listdir(folder_path), key=extract_number):
            file_path = join(folder_path, filename)  # Full path to the file
            if isfile(file_path) and not filename.startswith('.'):  # Check if it's a file and not a directory

                extension = filename.split('.')[-1]
                new_name = f"{foldername}_{count}.{extension}"  # New file name
                dst = join(folder_path, new_name)  # Destination path
                
                #print('dest', dst)
                
                # Uncomment the next line to actually rename the files
                
                os.rename(file_path, dst)
                
                #print(f'Renamed {file_path} to {dst}')  # Print the renaming action
                count += 1  # Increment the count for the next file
