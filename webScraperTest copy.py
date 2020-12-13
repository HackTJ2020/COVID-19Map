import urllib.request
import csv
from datetime import date
import datetime

target_url = 'https://data.cdc.gov/resource/9mfq-cb36.json?$select=new_case&submission_date='
date = str(date.today() - datetime.timedelta(days=1)) + 'T00:00:00.000'
state_names = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#for state in state_names:
#    final_url = target_url+date+"&state="+state
#    data = urllib.request.urlopen(final_url)
#    for line in data:
#        print(line.decode())
date = datetime.date(2020, 3, 1)
state = "VA"
with open("virginia_covrec.csv", 'w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Date", "New Cases"])
    x=1
    while(date<date.today()):
        final_url = target_url+str(date)+"&state="+state
        data = urllib.request.urlopen(final_url)
        for line in data:
            string = line.decode()
            string = string[14:]
            string = string[:-4]
            writer.writerow([date, float(string)])
        date= date+datetime.timedelta(days=1)
        x+=1