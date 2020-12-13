import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("csvFiles/VA_covrec3.csv", delimiter=',')
plt.plot(data)
plt.savefig("VAcovid.jpg")