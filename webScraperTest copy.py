import urllib.request

target_url = 'https://data.cdc.gov/resource/9mfq-cb36.json?submission_date='
date = '2020-11-24T00:00:00.000'
state = "VA"
final_url = target_url+date+"&state="+state
data = urllib.request.urlopen(final_url)
for line in data:
    print(line.decode())