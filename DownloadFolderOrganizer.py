"""
File Title:
  Download Folder Organizer.py

File Description:
    This a python script that organizes the files in the TARGET_DIRECTORY (passed in the 1st argument) based off the DIRECTORIES array.

File Author:
    Gabriel Goldstein

File Created Date:
    December 23, 2019
"""

import sys
import os
from pathlib import Path
from datetime import datetime
 
#Mapping of Folder names to file types.
#   "FOLDER_NAME" : ["FILE_TYPE","FILE_TYPE","FILE_TYPE"],
DIRECTORIES = {
    "Executables": [".exe", ".msi"],
    "TextFiles": [".txt"],
    "Images": [".png", ".jpg"],
    "Video": [".mp4"],
    "Scripts": [".ps1", ".js"],
    "DLLs": [".dll"],
    "ZIPs": [".zip"]
}

#Array function for pulling the file formats out of the DIRECTORIES array
FILE_FORMATS = {
    file_format: directory
    for directory, file_formats in DIRECTORIES.items()
    for file_format in file_formats
}
 
#The target directory where you want to organize the files. Passed in the 1st argument
TARGET_DIRECTORY = sys.argv[1]

#Function that will try to move the currently file into its intended folder based on the mapping
def move_file(original_path, dir_path, name, title, suffix):
    #If an error occurs, add datetime to the end of the file name 
    #   EX: testDocument.txt -> testDocument2019-12-25_10:55:32.txt
    try:
        original_path.rename(dir_path.joinpath(name))
    except WindowsError:
        original_path.rename(dir_path.joinpath(title + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + suffix))

#Function that will organize the files in the Target Directory
def organize_junk(path):
    for entry in os.scandir(path):
        if entry.is_dir():  #Checks if the entry is a directory
            continue

        #Capturing the File path, name(with extension), title(without extension), & format of the file found
        file_path = Path(entry)
        file_name = file_path.name
        file_name_title = file_name.split('.')[0]
        file_format = file_path.suffix.lower()

        print(f"Proccessing file: {file_name}")

        #If this file_format exists in the FILE_FORMAT array
        # THEN place the file based on the DIRECTORIES mapping
        # ELSE place the file in the MISC folder
        if file_format in FILE_FORMATS:
            directory_path = Path(path + "/" + FILE_FORMATS[file_format]) #Creates a full path for the directory
            directory_path.mkdir(exist_ok = True)   #Creates a directory if it does not already exist

            #Tries to move the file
            move_file(file_path, directory_path, file_name, file_name_title, file_format)
        else:
            misc_path = Path(path + "/Misc/")
            misc_path.mkdir(exist_ok = True)

            #Tries to move the file
            move_file(file_path, misc_path, file_name, file_name_title, file_format)             

#Main Function that is called on file execution (File Entry Point)
if __name__ == "__main__":
    print(f" === Starting 'Download Folder Organizer' ===")
    organize_junk(TARGET_DIRECTORY)    #Manually calls the organize_junk function
    print(f" === Task Finished === ")

