import urllib.request
from datetime import date
import datetime

target_url = 'https://data.cdc.gov/resource/9mfq-cb36.json?submission_date='
date = str(date.today() - datetime.timedelta(days=1)) + 'T00:00:00.000'
state_names = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

for state in state_names:
    final_url = target_url+date+"&state="+state
    data = urllib.request.urlopen(final_url)
    for line in data:
        print(line.decode())