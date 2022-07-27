import os 
import datetime
import sys 
import tarfile

def backup(jaar):
    files = (os.listdir())
    lst = []
    isexist = os.path.exists(jaar)

    for file in files: 
        c_time = os.path.getctime(file)
        dt_c = datetime.datetime.fromtimestamp(c_time).year

        if dt_c == int(jaar):
             lst.append(file)

    if lst:
        print('searching for backup archive from ' + jaar +'... found.')
    else:
        print('geen files gevonden')

    if not isexist:
        os.makedirs(str(jaar))
        print('Creating Directory ' + jaar +'.... done')

    for file in lst:
        if file.endswith('tar.gz'):
            tar = tarfile.open(file, 'r:gz')
            tar.extractall(jaar)
            tar.close()
            print('backup extracted successfully!')

        if file.endswith('.txt'):
            print('Showing backup notes:')
            f = open(file, 'r')
            file_content = f.read()
            print(file_content)



if len(sys.argv) == 2:
    jaar = sysargv[1]

else:
    jaar = input('Welk jaar?')

backup(jaar)

