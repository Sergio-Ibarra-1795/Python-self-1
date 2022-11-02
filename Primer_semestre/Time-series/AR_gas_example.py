from matplotlib.lines import lineStyles
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import datetime
from datetime import timedelta
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sympy import true
register_matplotlib_converters()
from time import time 

def parser(s):
    return datetime.strptime(s, '%m/%d/%Y')

##read data 
demanda_petrolero = pd.read_csv(R'Demanda_petrolero.csv', parse_dates=[0], index_col=0, squeeze=true, date_parser=parser, encoding = 'utf-8')


#Rename demand data 
demanda_petrolero.rename('demanda', inplace= True)
print(demanda_petrolero.head())


## Ploting the data 2005 onwards 
plt.figure(figsize=(10,4))
plt.plot(demanda_petrolero)
plt.title('Demanda de gas natural en sector petrolero', fontsize=20)
plt.ylabel('Demanda', fontsize =16)
for year in range(2005,2020):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--')

plt.show()