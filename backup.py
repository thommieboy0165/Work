import os
import datetime
import shutil
import tarfile
import sys 

def backup(jaar):
   
    files =(os.listdir())
    listfiles = []
    isexist = os.path.exists(jaar)

    for file in files: 
        c_time = os.path.getctime(file)
        dt_c = datetime.datetime.fromtimestamp(c_time).year
       

        if dt_c == int(jaar):
            listfiles.append(file)
       
    if listfiles:
        print('searching for backup archive from' + jaar +'... found.')
     
    if not isexist:
        os.makedirs(str(jaar))
        print('Creating Directory' + jaar +'.... done')

    for file in listfiles:
        if file.endswith('tar.gz'):
            tar = tarfile.open(file, "r:gz")
            tar.extractall(jaar)
            tar.close()
            print('Backup extracted successfully!')

         if file.endswith('.txt'):
            f = open(file, 'r')
            file_contents = f.read()
            print(file_contents)



if len(sys.argv) == 2:
    jaartje = sysargv[1]

else: 
    jaartje = input('welk jaar:')

backup(jaartje)
