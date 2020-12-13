import urllib.request
import csv
from datetime import *
import datetime

def create_CSV(state):
    target_url = 'https://data.cdc.gov/resource/9mfq-cb36.json?$select=new_case&submission_date='
    date = str(12/12/2020.today() - datetime.timedelta(days=1)) + 'T00:00:00.000'

    dat = datetime.date(2020, 3, 1)

    with open("csvFiles/" + state + "_covrec.csv", 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Date", "New Cases"])
        x=1
        while(dat<date.today()):
            final_url = target_url+str(date)+"&state="+state
            data = urllib.request.urlopen(final_url)
            for line in data:
                string = line.decode()
                string = string[14:]
                string = string[:-4]
                writer.writerow([date, float(string)])
            date= date+datetime.timedelta(days=1)
            x+=1



#for state in state_names:
#    final_url = target_url+date+"&state="+state
#    data = urllib.request.urlopen(final_url)
#    for line in data:
#        print(line.decode())

