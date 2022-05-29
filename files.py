import os
import datetime

def files_stats(path):
    
    files = [f for f in os.listdir(path) if os.path.isfile(f)]
    lijst = []

    for file in files:

        #ophalen creation time van file
        tijd = os.path.getctime(file)
        #Tijd omzetten naar leesbare tijdstamp
        c_tijd  = datetime.datetime.fromtimestamp(tijd)
        #Filteren op jaar 
        c_year = c_tijd.strftime("%Y")

        if c_year == '2022':
            #file samenvoegen in dict
            lijst.append({file:[c_year]})

    return(lijst)
#for item in os.scandir():
#    print(item)
#    file = os.path.getctime(item)
#    created  =  datetime.datetime.fromtimestamp(file)
#    print(item, created)


test = files_stats('.')
