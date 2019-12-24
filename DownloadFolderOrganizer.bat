REM This Batch file can be use:
REM     In the Task Scheduler 
REM     OR as a user shortcut to run the script

@echo off
REM Generic Python script file location
cd C:/Python/Scripts

REM PythonScriptFile, TargetDirectory
python DownloadFolderOrganizer.py "C:/Users/%username%/Downloads"

pause