import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
register_matplotlib_converters()
import csv

#Ice Cream Production Data 

#Read production data 
df_ice_cream = pd.read_csv(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Python-Self-Dell\Python-self-1\Pirmer_semestre\Time-series\ice_cream.csv')
print(df_ice_cream.head())


#rename columns to something more understandable
df_ice_cream.rename(columns={'DATE':'date', 'IPN31152N':'production'}, inplace=True)
print(df_ice_cream.head())

#convert date column to datetime type
df_ice_cream['date'] = pd.to_datetime(df_ice_cream.date)


#set date as index
df_ice_cream.set_index('date', inplace=True)


#just get data from 2010 onwards
start_date = pd.to_datetime('2010-01-01')
df_ice_cream = df_ice_cream[start_date:]

#show result
df_ice_cream.head()
print(df_ice_cream.head())


#Ploting the time-serie
plt.figure(figsize=(10,4))
plt.plot(df_ice_cream.production)
plt.title('Ice Cream Production over Time', fontsize=20)
plt.ylabel('Production', fontsize=16)
for year in range(2011,2021):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)


#Ploting the ACF 
acf_plot = plot_acf(df_ice_cream.production.dropna(), lags=100)


#Based on decaying ACF, we are likely dealing with an Auto Regressive process


#Ploting the PACF 
pacf_plot = plot_pacf(df_ice_cream.production.dropna())
plt.show()

#Based on PACF, we should start with an Auto Regressive model with lags 1, 2, 3, 10, 13