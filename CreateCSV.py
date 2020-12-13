def create_CSV(state):
    import urllib.request
    import csv
    from datetime import date
    import datetime
    target_url = 'https://data.cdc.gov/resource/9mfq-cb36.json?$select=new_case&submission_date='
    today = date.today()
    date = datetime.date(2020, 3, 1)
    fil = state+"_covrec.csv"
    with open("csvFiles/"+fil, 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Date", "New Cases"])
        while(date<today):
            dat = str(date) + 'T00:00:00.000'
            final_url = target_url+str(dat)+"&state="+state
            data = urllib.request.urlopen(final_url)
            for line in data:
                string = line.decode()
                string = string[14:]
                string = string[:-4]
                try:
                    writer.writerow([date, float(string)])
                except:
                    continue
            date= date+datetime.timedelta(days=1)
#for state in state_names:
#    final_url = target_url+date+"&state="+state
#    data = urllib.request.urlopen(final_url)
#    for line in data:
#        print(line.decode())

