#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:09:34 2024

@author: danielferreira
"""

# Pre-Process
import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text, plot_tree
import matplotlib.pyplot as plt
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
# The default Regression Tree usually split too far and is prune to overfitting
model1 = DecisionTreeRegressor()
model1.fit(X,y)
pred = model1.predict(X)
print(explained_variance_score(y,pred))

#%%
# You can see the rules with export_text
tree_rules = export_text(model1, feature_names=list(X.columns))
print(tree_rules)

#%%
# To control the size of the tree we can use max_depth
model2 = DecisionTreeRegressor(max_depth=4)
model2.fit(X,y)
pred = model2.predict(X)
print(explained_variance_score(y,pred))

#%%
# To see the tree you can use plot_tree
plt.figure(figsize=(20,10))
plot_tree(model2, filled=True, feature_names=list(X.columns), rounded=True)
plt.show()
