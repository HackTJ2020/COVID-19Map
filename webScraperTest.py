import urllib.request

target_url = 'https://data.cdc.gov/resource/9mfq-cb36.json?submission_date=2020-12-01T00:00:00.000'
data = urllib.request.urlopen(target_url)
for line in data:
    print(line)
