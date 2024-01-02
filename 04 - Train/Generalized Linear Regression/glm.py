#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:58:25 2024

@author: danielferreira
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import os
folder = '/Users/danielferreira/Documents/repositories/pySETTV/06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
index = 'player_id'
os.chdir(folder)
bat = pd.read_csv(file, index_col=index)

#%%
# Data pre-process
train = bat[bat['year']==2021]
test = bat[bat['year']==2022]
y_train = train['triple'].copy()
X_train = train[['sprint_speed','exit_velocity_avg', 'hr_10']].copy()
X_train['sprint_speed'] = X_train['sprint_speed'].fillna(X_train['sprint_speed'].median())
X_train['exit_velocity_avg'] = X_train['exit_velocity_avg'].fillna(X_train['exit_velocity_avg'].median())
y_train = np.array(y_train,dtype=float)
X_train = np.array(X_train,dtype=float)
X_train = sm.add_constant(X_train) 
y_test = test['triple'].copy()
X_test = test[['sprint_speed','exit_velocity_avg', 'hr_10']].copy()
X_test['sprint_speed'] = X_test['sprint_speed'].fillna(X_test['sprint_speed'].median())
X_test['exit_velocity_avg'] = X_test['exit_velocity_avg'].fillna(X_test['exit_velocity_avg'].median())
y_test = np.array(y_test,dtype=float)
X_test = np.array(X_test,dtype=float)
X_test = sm.add_constant(X_test) 

#%%
# Fitting a Normal Linear Regression
model1 = sm.OLS(y_train,X_train).fit()
model1.summary()

#%%
# Quick Fit Stat
pred_test = model1.predict(X_test)
residuals_test = y_test - pred_test
MAE = abs(residuals_test).mean()
print(f'Mean Absolute Error on Test = {round(MAE,3)}')

#%%
# The model seems fine, regards x2 (exit_velocity_avg) doesn't seem significant. 
# When we check model assumptions we see that the error is far from normal. So the parameters p-values may not make sense (they don't follow a t distribution as supposed)
residuals = model1.resid
predicted_values = model1.fittedvalues
plt.figure(figsize=(5, 3))
sns.scatterplot(x=predicted_values, y=residuals)
plt.title('Residuals vs. Fitted Values')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.show()
plt.figure(figsize=(5, 3))
sns.histplot(residuals, kde=True)
plt.title('Histogram of Residuals')
plt.xlabel('Residuals')
plt.show()

#%%
# GLM can help. Let's try using a Poisson Distribution.
model2 = sm.GLM(y_train, X_train, family=sm.families.Poisson())
result = model2.fit()
result.summary() 

#%%
# This function can help assessing statsmodel models
def quick_assess():
    result.summary()
    residuals = result.resid_deviance
    pred_test = result.predict(X_test)
    residuals_test = y_test - pred_test
    MAE = abs(residuals_test).mean()
    print(f'Mean Absolute Error on Test = {round(MAE,3)}')
    plt.figure(figsize=(5, 3))
    sns.histplot(residuals, kde=True)
    plt.title('Histogram of Residuals')
    plt.xlabel('Residuals')
    plt.show()
    
#%%
# Calling the function. Much better model, x2 is now significant and MAE decreased in Test Data
quick_assess()

#%%
# We can also change the link function. Let's try a Gamma with Log link function
model3 = sm.GLM(y_train, X_train,family=sm.families.Gamma(link=sm.families.links.Log()))
result = model3.fit()
print(result.summary())
quick_assess()

#%%
# Negative Binomial
model4 = sm.GLM(y_train, X_train,family=sm.families.NegativeBinomial(alpha=0.1))
result = model4.fit()
print(result.summary())
quick_assess()

#%%
# You can find all the families suported here:
# https://www.statsmodels.org/stable/glm.html#module-reference
