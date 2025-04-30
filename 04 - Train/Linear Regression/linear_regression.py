#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 19:20:38 2023

@author: danielferreira
"""
import numpy as np
import pandas as pd
import os
folder = '../../06 - Utility & References/Data'
file = 'bat_22_clean.csv'
index = 'player_id'
os.chdir(folder)
bat_22 = pd.read_csv(file, index_col=index)

#%%
# Simple Linear Regression

#%%
# Using scipy you can get a return with many usual stats and attributes of a model
from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(x=bat_22['batting_avg'], y=bat_22['y_2023_avg'])

#%%
# Visual Simple Linear Regression using seaborn
import seaborn as sns
import matplotlib.pyplot as plt
sns.regplot(data=bat_22, x='batting_avg', y='y_2023_avg')
plt.xlabel('Batting Average 2022')
plt.ylabel('Batting Average 2023')
plt.title(f'Y = {round(slope,2)} + {round(intercept,2)}*X') 
plt.annotate(f'R Squared = {round(r_value**2,3)}', xy=(0.05, 0.89), xycoords='axes fraction')
plt.show()

#%%
# statsmodels use a classic format, looking more like SAS, SPSS and R
import statsmodels.api as sm
X = bat_22['batting_avg']
X = sm.add_constant(X) #statsmodel expect to have a constant in the inputs if you want intercept estimation
y = bat_22['y_2023_avg']
model1 = sm.OLS(y, X).fit()
model1.summary()

#%%
# sklearn use a different approach. The model doesn't spit reports like statmodels (and r, sas and spss)
from sklearn.linear_model import LinearRegression
X = np.array(bat_22['batting_avg']).reshape(-1,1) # reshape is needed because sklearn always expect 2D arrays (for multiple linear regression)
y = bat_22['y_2023_avg']
model2 = LinearRegression()
model2.fit(X,y) # Fits model
y_pred = model2.predict(X) # Create predictions

#%%
# Sklearn

#%%
# If you want outputs you can get it from the model attributes:
print(f'Coefficients of the model = {model2.coef_}')
print(f'Intercept = {model2.intercept_}')

#%%
# It is easy to calculate certain fit statistics. For example Rˆ2:
residuals = y - y_pred
total_var = y - y.mean()
SSE = np.dot(residuals,residuals)
SST = np.dot(total_var,total_var)
n = len(y)
k = X.shape[1]+1 # +1 for intercept
R2 = 1-(SSE/SST)
print(f'R Squared = {round(R2,3)}')
Adj_R2 = 1-((SSE/(n-k))/(SST/(n-1)))
print(f'Adjusted R Squared = {round(Adj_R2,3)}')

#%%
# sklearn also have many methods that can help with fit statistics
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
mse = mean_squared_error(y, y_pred)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)
print("Mean Squared Error (MSE):", round(mse,4)) # Usually calculated with test data sets
print("Mean Absolute Error (MAE):", round(mae,4)) # Usually calculated with test data sets
print("R-squared:", round(r2,3))

#%%
# Residuals: Residuals vs Predictions
plt.scatter(y_pred,residuals)
plt.title('Residual vs Prediction')
plt.xlabel('Predictions')
plt.ylabel('Residuals')

#%%
# Residuals: Residuals vs Input. Not very useful for Simple Linear Regression
plt.scatter(X, residuals)
plt.title('Residual vs X')
plt.xlabel('Batting Avg 2022')
plt.ylabel('Residuals of Batting Avg 2023 Predictions')

#%%
# Residuals Normality
from scipy.stats import norm
sns.histplot(x = residuals, kde=True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, np.mean(residuals), np.std(residuals))
plt.plot(x, p, color='red') # Theorectical Normal Dist
plt.title('Residuals Distribution')
plt.show()
sm.qqplot(residuals, line='s', loc=0)
plt.title('Residuals QQ Plot')
plt.show()

#%%
# Multiple Linear Regression is exaclty the same, you don't even need to reshape the array
# I will redo all the steps using train and test splits and multiple regression so we can reuse the code with real world data. 

#%%
# Fitting, Predicting and getting coefs work just like simple linear regression
inputs = ['player_age','ab', 'hit', 'home_run', 'k_percent','batting_avg','sprint_speed']
outcome = 'y_2023_avg'
X = bat_22[inputs]
y = bat_22['y_2023_avg']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.75 , random_state = 0)
model3 = LinearRegression()
model3.fit(X_train,y_train) # Fits model
y_pred_train = model3.predict(X_train) # Create predictions on Train
y_pred_test = model3.predict(X_test) # Create predictions on Test
print(f'Coefficients of the model = {model3.coef_}')
print(f'Intercept = {model3.intercept_}')

#%%
# Residuals Calc
residuals_train = y_train - y_pred_train
residuals_test = y_test - y_pred_test

#%%
# Fit Statistics
mse = mean_squared_error(y_test, y_pred_test)
mae = mean_absolute_error(y_test, y_pred_test)
r2 = r2_score(y_test, y_pred_test)
print("Mean Squared Error (MSE) - Test Data:", round(mse,4)) # Usually calculated with test data sets
print("Mean Absolute Error (MAE) - Test Data:", round(mae,4)) # Usually calculated with test data sets
print("R-squared - Test Data:", round(r2,3))

#%%
# Residual Plots
plt.scatter(y_pred_train,residuals_train)
plt.title('Residual vs Prediction')
plt.xlabel('Predictions')
plt.ylabel('Residuals')

#%%
# Residual vs Inputs:
for x in inputs:
    plt.scatter(X_train[x],residuals_train)
    plt.title(f'Residual vs {x}')
    plt.xlabel(x)
    plt.ylabel('Residuals')
    plt.show()
    
#%%
# Residuals Normality
sns.histplot(x = residuals_train, kde=True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, np.mean(residuals_train), np.std(residuals_train))
plt.plot(x, p, color='red') # Theorectical Normal Dist
plt.title('Residuals Distribution - Train')
plt.show()
sm.qqplot(residuals, line='s', loc=0)
plt.title('Residuals QQ Plot - Train')
plt.show()

#%%
# Feature Selection: LASSO
from sklearn.linear_model import Lasso
X = bat_22[inputs]
y = bat_22['y_2023_avg']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.75 , random_state = 0)
model4 = Lasso()
model4.fit(X_train,y_train) # Fits model
y_pred_train = model4.predict(X_train) # Create predictions
y_pred_test = model4.predict(X_test) # Create predictions
print(f'Coefficients of the model = {model4.coef_}')
print(f'Intercept = {model4.intercept_}')

#%%
# Feature Selection: Forward
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
model5 = LinearRegression()
sfs = SFS(model5,k_features=X_train.shape[1],forward=True, verbose=2) # verbose = 2 shows wach step
sfs = sfs.fit(X_train, y_train)
