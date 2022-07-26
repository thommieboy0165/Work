import os

file = input('Wat is de naam van de file:')

lijst = []
lijst.append(file)

os.chmod(file, 0o755) 



