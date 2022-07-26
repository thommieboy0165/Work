import tarfile 
import sys

def unzip(filenaam):
    if filenaam.endswith("tar.gz"):
        tar = tarfile.open(filenaam, "r:gz")
        tar.extractall()
        tar.close
    elif filenaam.endswith("tar"):
        tar = tarfile.open(filenaam, "r:")
        tar.extractall()
        tar.close()

if len(sys.argv) == 2:
    file = sys.argv[1]

else:
    file = input('Wat is de file naam: ')

unzip(file)

