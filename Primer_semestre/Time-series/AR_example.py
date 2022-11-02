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
#production_ice_cream = pd.read_csv(R'C:\Users\sergi\OneDrive\Documentos\SIR_personal\Python-Self-HP\Python-self-1\Primer_semestre\Time-series\ice_cream.csv', parse_dates=[0], index_col=0, squeeze=true, date_parser=parser, encoding = 'utf-8')
production_ice_cream = pd.read_csv(R'ice_cream.csv', parse_dates=[0], index_col=0, squeeze=true, date_parser=parser, encoding = 'utf-8')

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

#plt.show()

##BASED on PACF function we shoul start with an AR model with lags 1,2,3

## Get training and testing sets 
train_end = datetime(2018,12,1)
test_end = datetime(2019,12,1)
##This means we are taking from 2010 to 2018 as traning data to predict 2019

train_data = production_ice_cream[:train_end]
test_data = production_ice_cream[train_end+ timedelta(days=1):test_end]

## Fit the AR Model 
##Create the model
model = ARIMA (train_data, order=(3,0,0))

##Fit the model
start = time()
model_fit = model.fit()
end = time()
print('Model fitting time', end-start)


##Summary of the model 
print(model_fit.summary())

##get prediction start and end dates 
pred_start_date = test_data.index[0]
pred_end_date = test_data.index[-1]

##get the predictors and residuals 
predictions = model_fit.predict(start=pred_start_date, end= pred_end_date)
residuals = test_data - predictions 

##Ploting the residuals 
plt.figure(figsize =(10,4))
plt.plot(residuals)
plt.title('Residuals from AR Model', fontsize=20)
plt.ylabel('Error', fontsize=16)
plt.axhline(0, color='r', linestyle='--', alpha=0.2)
for year in range(2019,2021):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--')


##Ploting the predicitons vs the test_data
plt.figure(figsize =(10,4))
plt.plot(test_data)
plt.plot(predictions)
plt.legend(('Data', 'Predictions'), fontsize=16)

plt.title('Ice cream production test_data & predicitons AR(3) model', fontsize=20)
plt.ylabel('Production', fontsize=16)
for year in range(2019,2021):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--')

#plt.show()

##Printing some metrics 
print('Mean abosulute Percent error:', round(np.mean(abs(residuals/test_data)),4))

print('Root Mean Squared Error:', np.sqrt(np.mean(residuals**2)))

