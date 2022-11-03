import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima.model import ARIMA
from sympy import true
from datetime import datetime, timedelta
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
plt.ylabel('Demanda [MMpcd]', fontsize =16)
for year in range(2005,2021):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--')


#Ploting the ACF (Autocorrelation function)
acf_plot = plot_acf(demanda_petrolero.dropna(), lags=100)

#Ploting the PACF (Partial Autocorrelation function)
pacf_plot = plot_pacf(demanda_petrolero.dropna())


##BASED on PACF function we shoul start with an AR model with lags 1,2 or 5 

## Get training and testing sets 
train_end = datetime(2018,12,1)
test_end = datetime(2024,12,1)
##This means we are taking from 2005 to 2018 as traning data to predict 2019 and 2020

train_data = demanda_petrolero[:train_end]
test_data = demanda_petrolero[train_end+ timedelta(days=1):datetime(2023,10,1)]

##get prediction start and end dates 
pred_start_date = test_data.index[0]
pred_end_date = test_data.index[-1]


## Fit the AR Model 

##Create the model and making just one prediction for iteration and then the next prediction and so on 

predictions_rolling = pd.Series()
for end_date in test_data.index:
    train_data = demanda_petrolero[:end_date - timedelta(days=1)]
    model = ARIMA (train_data, order=(5,0,10))
    model_fit = model.fit()
    pred = model_fit.predict(end_date)
    predictions_rolling.loc[end_date] = pred.loc[end_date]


residuals_rollling = test_data - predictions_rolling 


##Summary of the model 
print(model_fit.summary())

##Ploting the residuals 
plt.figure(figsize =(10,4))
plt.plot(residuals_rollling)
plt.title('Residuals from ARMA Model', fontsize=20)
plt.ylabel('Error', fontsize=16)
plt.axhline(0, color='r', linestyle='--', alpha=0.2)
for year in range(2019,2020):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--')



##Ploting the predicitons vs the test_data
plt.figure(figsize =(10,4))
plt.plot(test_data)
plt.plot(predictions_rolling)
plt.legend(('Data', 'Predictions'), fontsize=16)

plt.title('Demanda sector petrolero test_data & predicitons ARMA(5,0,10) model', fontsize=20)
plt.ylabel('Demanda [MMpcd]', fontsize=16)
for year in range(2019,2024):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--')


##Printing some metrics 
print('Mean abosulute Percent error:', round(np.mean(abs(residuals_rollling/test_data)),4))

print('Root Mean Squared Error:', np.sqrt(np.mean(residuals_rollling**2)))


plt.show()