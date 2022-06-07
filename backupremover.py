import os

files = os.listdir()
list = []
    
    for file in files:
        print(file)

list.append("backup.20141101.tar.gz")
list.append("backup.20171101.tar.gz")
list.append("backup.20151101.tar.gz")

list.sort()

for l in list:
    if l == list[-1]:
        print ("[keep]", l)
        
    else:
        print ("[remove]", l)

















#Legacy backup remover

#Assume backups are stored in files with the following naming scheme:

#backup_yyyymmdd.tar.gz

#Create a script that lists all backup files in a certain directory.
#In the script output, mark each file as either "keep" or "delete".

#Example output:

#$ ./legacy_backup_remover.py
#Using scheme: backup_yyyymmdd.tar.gz
#[delete] backup_20141101.tar.gz
#[delete] backup_20141201.tar.gz
#[keep]   backup_20150101.tar.gz
#$ 

#Only the most recent file can (and must) be marked as "keep".

#Choose a file to upload. (Maximum file size: 20MB)
#File: 
