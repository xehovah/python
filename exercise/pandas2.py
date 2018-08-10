from __future__ import print_function
from IPython import display
from matplotlib import cm
from matplotlib import gridspec
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gdp = pd.read_csv('GDP(PPP).csv')
gdp_pc=pd.read_csv('GDP(PPP)_per_Capita.csv')
"""
plt.figure(figsize=(15,6))
plt.title("GDP(PPP) per Capita")
plt.ylabel("INT$")
plt.xlabel("Country")
plt.bar(gdp_pc['Country'].head(30), gdp_pc['INT'].head(30))
plt.show()
"""
t=gdp_pc.plot()
t.show()
