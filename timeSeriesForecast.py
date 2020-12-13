import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

df = pd.read_csv("virginia_covrec.csv")
cases = df
cases["Date"] = pd.to_datetime(cases["Date"])
cases = cases.set_index("Date")
print(cases.index)
y=cases["New Cases"].resample('MS').mean()
y.plot(figsize=(15,6))
plt.show()