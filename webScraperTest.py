import urllib.request

target_url = 'https://data.cdc.gov/resource/9mfq-cb36.json?submission_date=%272020-1-24T00:00:00.000%27&state=VA'
data = urllib.request.urlopen(target_url)
for line in data:
    print(line)