import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.head(5)

x=df["Country Name"]
y=df["2005 [YR2005]"]
plt.plot(x,y)
plt.show()