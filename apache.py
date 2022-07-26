import subprocess

services = ['apache2']
for service in services:
    try:
        status = subprocess.check_output("/etc/init.d/"+service+" status", shell=True)
        print('Apache is running') 
    except subprocess.CalledProcessError as e:
        status = "is stopped"
        print(status)
