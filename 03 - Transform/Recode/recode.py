#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:45:45 2023

@author: danielferreira
"""
#%%
# Many times our variables/features/columns need recoding. Let's cover some of the cases where recoding would be benefit for your ML Model:
# * Categorical columns need to be transformed into numerical columns to be used in formula-based algorithms (Regressions, NN, SVM, k-NN and many others):
#  - One-Hot Encodding: Binary Dummies for each category.
#  - Label Encoding: Simple Mapping of values (A -> 1, B -> 2).
# * Categorical columns have huge cardinality (too many categories) and grouping them can be beneficial to avoid curse of dimensionality.
# * Numerical input features have complex relantionships with outcome and categorizing them before one-hot encoding can simplify things.
# * Windowing: Imputation of outliers.
# * Complex cases depending on multiple variables

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
# Categorical columns need to be transformed into numerical columns to be used in formula-based algorithms
# * One-Hot Encodding: Binary Dummies for each category.
# * Label Encoding: Simple Mapping of values (A -> 1, B -> 2).

#%%

#%%
# One-Hot Encodding: Binary Dummies for each category
hot_c = ['division', 'league']
new_bat = pd.get_dummies(data=bat, columns=hot_c, drop_first=True)
# This code is only if you want to see results
new_bat['division']=bat['division']
new_bat['league']=bat['league']
selected_columns = [col for col in new_bat.columns if any(col.startswith(prefix) for prefix in hot_c)]
new_bat[selected_columns].head()

#%%
# drop first don't create dummy for the first category of each column, if you want it all (be carefull with multicolinearity) you can use drop_first=False
new_bat = pd.get_dummies(data=bat, columns=hot_c, drop_first=False)
# This code is only if you want to see results
new_bat['division']=bat['division']
new_bat['league']=bat['league']
selected_columns = [col for col in new_bat.columns if any(col.startswith(prefix) for prefix in hot_c)]
new_bat[selected_columns].head()

#%%
# Label Encoding: Simple Mapping of values (A -> 1, B -> 2)
# That is usually not the best approach. Only in cases where you have an ordinal variable and it is fair to assume the have someking of linear relationship with the outcome.
new_bat['division_num'] = new_bat['division'].map({'NLW':0, 'ALC':1, 'NLE':2, 'NLC':3, 'ALW':4, 'ALE':5})
new_bat[['division_num','division']].head()
# map can be very usefull in other scenarios as well, you just need to input a dictionary and he will make a translation

#%%
# Categorical columns have huge cardinality (too many categories) and grouping them can be beneficial to avoid curse of dimensionality.
new_bat['league_v2'] = new_bat['division'].map({'NLW':'NL', 'ALC':'AL', 'NLE':'NL', 'NLC':'NL', 'ALW':'AL', 'ALE':'AL'})
new_bat[['league_v2','division']].head()

#%%
# For some modeling cases, visualizing the proportion of your outcome can help deciding how to categorize them.
cross_tab = pd.crosstab(new_bat['team_name'], new_bat['hr_20'], normalize=0)
proportions = cross_tab.iloc[:,1].sort_values()
proportions.plot(kind = 'bar')

#%%
# Numerical input features have complex relantionships with outcome and categorizing them before one-hot encoding can simplify things.
new_bat['player_age_bin'] = pd.cut(new_bat['player_age'], bins=5)
new_bat[['player_age','player_age_bin']].head()

#%%
# If you don't want to use percentiles:
custom_ranges = [float('-inf'),20,30,40,float('inf')] 
labels = ['<20', '20-30', '30-40', '>40']
new_bat['player_age_bin'] = pd.cut(new_bat['player_age'], bins=custom_ranges, labels=labels, include_lowest=True)
new_bat[['player_age','player_age_bin']].head() 

#%%
# Windowing: Imputation/deletion of outliers.

#%%

#%%

# To delete observations greater than specific value you just need to input a boolean series
threshold = 0.32
cleaned_bat = bat[bat['batting_avg']>threshold]

#%%
# You can also use automate the deletion by using percentiles 
threshold = bat['batting_avg'].quantile(0.99)
cleaned_bat = bat[bat['batting_avg']>threshold]

#%%
# For recoding, the easiest way is to use minimun/maximun logic
bat['batting_avg_v2'] = np.minimum(bat['batting_avg'], threshold)

#%%
# Advanced Filters

#%%

#%%
# np.where can help with more advanced cases, where you depend on multiple columns, you can also nest np.where's
t1 = 0.31
t2 = 0.32
bat['batting_avg_v3'] = np.where( bat['league'] == 'AL', np.minimum(bat['batting_avg'],t1) , np.minimum(bat['batting_avg'],t2))
