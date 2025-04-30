#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:39:51 2023

@author: danielferreira
"""

#%%
# Standardization

#%%

#%%
# Import libs and data
import numpy as np
import pandas as pd
import os
folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
index = 'player_id'
os.chdir(folder)
bat = pd.read_csv(file, index_col=index)

#%%
# Pandas make it simple to do the most common standardizations, for instance minmax:
bat['player_age_minmax'] =  (bat['player_age']-bat['player_age'].min())/(bat['player_age'].max()-bat['player_age'].min())
bat[['player_age','player_age_minmax']].head()

#%%
# If you want to do with multiple columns, you might want to use a function:
def min_max_scaler(x):
    return (x-x.min())/(x.max()-x.min())
col_scale = ['player_age', 'ab', 'home_run', 'batting_avg']
for x in col_scale:    
    bat[x+'_minmax']= min_max_scaler(bat[x])
bat[['player_age', 'ab', 'home_run', 'batting_avg','player_age_minmax', 'ab_minmax', 'home_run_minmax', 'batting_avg_minmax']].head()

#%%
# The same can be done with other common standardization:
def normal_scaler(x):
    return (x-x.mean())/x.std()
col_scale = ['player_age', 'ab', 'home_run', 'batting_avg']
for x in col_scale:    
    bat[x+'_std']= normal_scaler(bat[x])
bat[['player_age', 'ab', 'home_run', 'batting_avg','player_age_std', 'ab_std', 'home_run_std', 'batting_avg_std']].head()

#%%
# sklearn have a lot of scaler methods. You can also use it:
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
col_scale = ['player_age', 'ab', 'home_run', 'batting_avg']
new_names = [col+'_minmax' for col in col_scale]
bat[new_names] = scaler.fit_transform(bat[col_scale])
bat[new_names].head()

#%%
# Standard Scaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
col_scale = ['player_age', 'ab', 'home_run', 'batting_avg']
new_names = [col+'_std' for col in col_scale]
bat[new_names] = scaler.fit_transform(bat[col_scale])
bat[new_names].head()

#%%
# Robust Scaler uses Q1 and Q3: (X-Q1)/(Q3-Q1)
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
col_scale = ['player_age', 'ab', 'home_run', 'batting_avg']
new_names = [col+'_rs' for col in col_scale]
bat[new_names] = scaler.fit_transform(bat[col_scale])
bat[new_names].head()

