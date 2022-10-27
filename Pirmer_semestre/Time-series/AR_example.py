from matplotlib.lines import lineStyles
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import datetime
from datetime import timedelta
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARMA
from sympy import true
register_matplotlib_converters()
from time import time 

def parser(s):
    return datetime.strptime(s, '%m/%d/%Y')

##read data 
production_ice_cream = pd.read_csv(R'C:\Users\sergi\OneDrive\Documentos\SIR_personal\Python-Self-HP\Python-self-1\Pirmer_semestre\Time-series\ice_cream.csv', parse_dates=[0], index_col=0, squeeze=true, date_parser=parser, encoding = 'utf-8')

production_ice_cream.rename('production', inplace= True)
#print(production_ice_cream.head())


## Infer the frequency of the data
#production_ice_cream = production_ice_cream.asfreq(pd.infer_freq(production_ice_cream.index))

## just get data from 2010 onwards 
start_date = pd.to_datetime('2010-01-01')
production_ice_cream = production_ice_cream[start_date:]
#print(production_ice_cream.head())

## Ploting the data 2010 onwards 

plt.figure(figsize=(10,4))
plt.plot(production_ice_cream)
plt.title('Ice Cream Production over Time', fontsize=20)
plt.ylabel('Production', fontsize =16)
for year in range(2010,2021):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--')

#Ploting the ACF (Autocorrelation function)
acf_plot = plot_acf(production_ice_cream, lags=100)

#Ploting the PACF (Partial Autocorrelation function)
pacf_plot = plot_pacf(production_ice_cream)


plt.show()

