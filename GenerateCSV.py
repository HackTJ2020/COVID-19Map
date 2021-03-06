def generateCSV():
    from CreateCSV import create_CSV
    import numpy as np
    import matplotlib.pyplot as plt

    state_names = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


    for state in state_names:
        create_CSV(state)
    for state in state_names:
        data = np.genfromtxt("csvFiles/" + state + "_covrec.csv", delimiter=',')
        plt.title(state+' COVID-19 Cases')
        plt.xlabel("Days after 03/01/2020")
        plt.ylabel("New Cases")
        plt.plot(data)
        plt.savefig("imgFiles/" + state + "covid.jpg")
        plt.close()