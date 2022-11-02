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

demanda_petrolero.rename('Demanda', inplace= True)

print(demanda_petrolero.head())


plt.figure(figsize=(10,4))
plt.plot(demanda_petrolero)
plt.title('Demanda de gas natural en el sector petrolero en México', fontsize=20)
plt.ylabel('Demanda ', fontsize =16)
for year in range(2005,2021):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--')


#Ploting the ACF (Autocorrelation function)
acf_plot = plot_acf(demanda_petrolero.dropna(), lags=100)

#Ploting the PACF (Partial Autocorrelation function)
pacf_plot = plot_pacf(demanda_petrolero.dropna())


plt.show()
