#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:22:17 2024

@author: danielferreira
"""

# Pre-Process
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import explained_variance_score
import os
folder = '/Users/danielferreira/Documents/repositories/pySETTV/06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
index = 'player_id'
os.chdir(folder)
bat = pd.read_csv(file, index_col=index)
outcome = bat[bat['year']==2023]['batting_avg']
bat_22 = bat[bat['year']==2022].copy()
bat_22['y_2023_avg'] = outcome
bat_22 = bat_22[bat_22['y_2023_avg'].isna()==False] # Those who weren't in 2023 MBL
bat_22 = bat_22.drop(['team_id','hp_to_1b'], axis=1)
cols = ['team_name','division','league']
for x in cols:
    bat_22[x] = bat_22[x].fillna('Free-Agent')
bat_22['sprint_speed'] = bat_22['sprint_speed'].fillna(bat_22['sprint_speed'].mean())
inputs = ['player_age','ab', 'hit', 'home_run', 'k_percent','batting_avg','sprint_speed']
X = bat_22[inputs]
y = bat_22['y_2023_avg']

#%%
# Default Gradient Boosting
model1 = GradientBoostingRegressor()
model1.fit(X,y)
pred = model1.predict(X)
print(explained_variance_score(y,pred))

#%%
# The default is trees with 3 floors, so you can make it even simpler with stumps (max_depth=2)
model2 = GradientBoostingRegressor(max_depth=2)
model2.fit(X,y)
pred = model2.predict(X)
print(explained_variance_score(y,pred))

#%%
# The default for number of threes is 100, you can increase with n_estimators
model3 = GradientBoostingRegressor(max_depth=2,n_estimators=400)
model3.fit(X,y)
pred = model3.predict(X)
print(explained_variance_score(y,pred)) # This metric should not be maximized, it will lead to overfit.

#%%
# If you want to understand what happens in each step
model4 = GradientBoostingRegressor(max_depth=2, n_estimators=400, verbose=1)
model4.fit(X,y)
pred = model4.predict(X)
print(explained_variance_score(y,pred))

#%%
# Some more options from:
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html
# loss{‘squared_error’, ‘absolute_error’, ‘huber’, ‘quantile’}, default=’squared_error’
# learning_rate float, default=0.1
# criterion{‘friedman_mse’, ‘squared_error’}, default=’friedman_mse’
# min_samples_split, min_samples_leaf
# validation_fraction float, default=0.1
