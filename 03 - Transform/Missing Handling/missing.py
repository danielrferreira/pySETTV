#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 11:47:09 2023

@author: danielferreira
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os
folder = '/Users/danielferreira/Documents/repositories/pySETTV/06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
index = 'player_id'
os.chdir(folder)
bat = pd.read_csv(file, index_col=index)

#%%
# To create a series with number of missings we can can combine isna() with sum()
bat.isna().sum()

#%%
# Percentages
bat.isna().sum()/len(bat)

#%%
# To see only the variables with missing
missing_percent = bat.isna().sum()/len(bat)
missing_percent[missing_percent>0]

#%%
# If you want to create a list with the columns we need to address
missing_c = list((missing_percent[missing_percent>0]).index)
missing_c

#%%
# Looking at the missingness distribution can help understand the best strategy
sns.kdeplot(missing_percent, bw_adjust=0.1)  # low bw_adjust makes kernel closer to observed distribution 
plt.suptitle("Distribution of %-missing values in each column")

#%%
# Missingness Relationship with outcome
# Sometimes the fact that the variable has a missing implies something related to the outcome.

#%%
# Binary Outcome
x = 'hp_to_1b'
data = bat
outcome = 'hr_10'
missing = data[x].isna()
cross_tab = pd.crosstab(missing, data[outcome])
cross_tab.plot(kind='bar')
plt.title(f'{x} missingness vs {outcome}')

#%%
# Quantitative Outcome
x = 'hp_to_1b'
data = bat
outcome = 'batting_avg'
missing = data[x].isna()
sns.kdeplot(data=data, x=outcome, hue=missing, common_norm=False)
plt.title(f'{x} missingness vs {outcome}')

#%%
# Check the Explore Bivariate Folder for functions to do the above with multiple variables at once, a simpler versions is just a for loop like this:
data = bat
outcome = 'hr_10'
for x in missing_c:
    missing = data[x].isna()
    cross_tab = pd.crosstab(missing, data[outcome])
    cross_tab.plot(kind='bar')
    plt.title(f'{x} missingness vs {outcome}')
    plt.show()

#%%
# Missing Imputation

#%%
# If missing are concentrated in one column, or the columns is useless you can just remove it from the table:
bat = bat.drop('team_id', axis=1)

#%%
# The most simple way to handle missing is creating a proper label for it, for instance, team related columns are missing because they are free agents
bat['imp_team_name'] = bat['team_name'].fillna('Free-Agent')

#%%
# Simple loop to do it with multiple columns
cols = ['team_name','division','league']
for x in cols:
    name = 'imp_'+x
    bat[name] = bat[x].fillna('Free-Agent')
    
#%%
# Another simple method is to use a single value based on the column, you can use median, mean, mode, min, max and any other summary stat
bat['imp_exit_velocity_avg'] = bat['exit_velocity_avg'].fillna(bat['exit_velocity_avg'].median())

#%%
# Distribution is a method that ensure the distribution before and after remains the same.
temp = pd.cut(bat['sprint_speed'], bins=10).value_counts(normalize=True)
centroids = [ (x.left+x.right)/2 for x in temp.index ] 
def fill_missing(value):
    if pd.isnull(value):
        return np.random.choice(centroids, p=temp)
    else:
        return value
bat['imp_sprint_speed_v1'] = bat['sprint_speed'].apply(lambda x: fill_missing(x))

#%%
# This code can show that before and after follow the same distribution
sns.histplot(data=bat['sprint_speed'], bins = 10)
plt.show()
sns.histplot(data=bat['imp_sprint_speed_v1'], bins = 10)
plt.show()

#%%
# If you want to see how it would be if we used mean for instance:
bat['imp_sprint_speed_v2'] = bat['sprint_speed'].fillna(bat['sprint_speed'].mean())
sns.histplot(data=bat['sprint_speed'], bins = 20)
plt.show()
sns.histplot(data=bat['imp_sprint_speed_v2'], bins = 20)
plt.show()
# This case didn't change much, because we only had 4% of missing, but if you have >10% you would note a bump in the mean bucket.

#%%
# Last, just to see the impact of distribution vs mean when we have a lot of missings:
var = 'hp_to_1b'
temp = pd.cut(bat[var], bins=10).value_counts(normalize=True)
centroids = [ (x.left+x.right)/2 for x in temp.index ] 
bat['imp_'+var+'_v1'] = bat[var].apply(lambda x: fill_missing(x))
bat['imp_'+var+'_v2'] = bat[var].fillna(bat[var].mean())
sns.histplot(data=bat[var], bins = 10)
plt.title('Original')
plt.show()
sns.histplot(data=bat['imp_'+var+'_v1'], bins = 10)
plt.title('Distribution based')
plt.show()
sns.histplot(data=bat['imp_'+var+'_v2'], bins = 10)
plt.title('Mean')
plt.show()

#%%
# Modeling approach. In this case I will use a very simple regression, but in the decision tree chapter we will come back to this application.
model = LinearRegression()
train = bat[['hp_to_1b','imp_sprint_speed_v1']].dropna(subset=['hp_to_1b']) #Create training dataframe without missings
x = np.array(train['imp_sprint_speed_v1']).reshape(-1, 1) # sklearn expects a multiple linear regression, so the input should be 2D array (why reshape)
y = np.array(train['hp_to_1b'])
model.fit(x,y)
slope = model.coef_[0] # If not a simple linear regression we need to revisit here
intercept = model.intercept_
bat['imp_hp_to_1b_v1'] = np.where(bat['hp_to_1b'].isna(), intercept+slope*bat['imp_sprint_speed_v1'],bat['hp_to_1b'])

#%%
# Just remember to have a look at fit statistics to see if it make sense the imputation
y_pred = model.predict(x)
r2 = r2_score(y, y_pred)
print(f'R-squared: {round(r2,3)}')
