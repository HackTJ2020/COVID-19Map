import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("virginia_covrec.csv", delimiter=',')
plt.plot(data)
plt.savefig("VAcovid.jpg")