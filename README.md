
# Description
"Download Folder Organizer" is a python script that when its run will organize the "TARGET_DIRECTORY" (in this case the Download Folder) based on the mapping provided in the "DIRECTORIES" array. This can be changed to any folder location if desired. I just used it for my Downloads folder.  

Included files are:  

    DownloadFolderOrganizer.py = The python script. Does all the work

    DownloadFolderOrganizer.bat = Calls the python script. (Optional - My version used in the Task Scheduler)

    Download Folder Organizer.xml = An export of the Task Scheduler task for use in importing the task. (Optional - My version of the scheduled task)

# Parameters
These are the parameters you will need to customize for your environment.

    TARGET_DIRECTORY = Folder location you want to organize (Passed as an argument to the python script)

    DIRECTORIES = The mapping of which file types belong to which folder (Variable in the python script)

# Usage
Running just the python script in the cmd line:

    python "[PYTHON_SCRIPT_LOCATION]/DownloadFolderOrganizer.py" "TARGET_DIRECTORY"

    # My Example
    python "C:/Python/Scripts/DownloadFolderOrganizer.py" "C:/Users/%username%/Downloads"

Running the script using the .bat file:

- Update DownloadFolderOrganizer.bat with the path to the python script as well as the Target Directory.  

        cd "[PYTHON_SCRIPT_LOCATION]" 
        python DownloadFolderOrganizer.py "TARGET_DIRECTORY"

Running the script as a Scheduled Task (Windows only):
- Open the "Task Scheduler" application
- In the right nav bar, click "Create Basic Task"
- Give the task a name and description
- Set up a trigger
- Action : Start a program
- Put the .bat file path as the "Program/script"
- Fin
- P.S. Make sure the path in the .bat file is pointing to the python file.
- P.S.S. You can use the "Download Folder Orgnaizer.xml" file to import my scheduled task. You would need to adjust the .bat file path.

 