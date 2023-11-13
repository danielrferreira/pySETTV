#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:46:08 2023

@author: danielferreira
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
folder = '/Users/danielferreira/Documents/repositories/pySTETV/06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
os.chdir(folder)
bat = pd.read_csv(file)
bat_22_23 = bat[bat['year'].isin([2023,2022])]

#%%
# This will used as examples of variables we want to understand
i = 'year'
j = 'hr_10'
data = bat_22_23

#%%
# Creates the crosstab
cross_tab = pd.crosstab(data[i], data[j])
# Creates a series with proportions of second category, usually True or 1
proportions = round((cross_tab[cross_tab.columns[1]]/cross_tab.sum(axis=1))*100,2)

#%%
# Chi-squared test
chi2, p = chi2_contingency(cross_tab)[0:2]
print(f'{i} vs {j}')
print(f'Chi-squared: {round(chi2,2)}')
if p<0.0001:
    print('p-value: <0.0001')
else:
    print(f'p-value: {round(p,4)}')

#%%
# One idea is to print count plots with proportions
print(f'{i} vs {j}')
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
cross_tab.plot(kind='bar', stacked=False,width=0.9, ax=axes[0])
d = proportions.plot(kind = 'bar',ax=axes[1])
d.bar_label(d.containers[0])
plt.title(f'Proportion of {j}={cross_tab.columns[1]} vs {i}')
plt.show()

#%%
# This function would do the trick for multiple variables
def cat_bivariate(data, col1, col2):
    '''Bivariate Analysis of two list of categorical columns
    
    Args:
        data: Data Frame
        col1: List of input categorical columns
        col2: List of outcome variables, should be low cardinality
    '''
    for i in col1:
        for j in col2:
            # Creates the crosstab
            cross_tab = pd.crosstab(data[i], data[j])
            # Creates a series with proportions of second category, usually True or 1
            proportions = round((cross_tab[cross_tab.columns[1]]/cross_tab.sum(axis=1))*100,2)
            # Chi-squared test
            chi2, p = chi2_contingency(cross_tab)[0:2]

            # Report
            print(f'{i} vs {j}')
            print(f'Chi-squared: {round(chi2,2)}')
            if p<0.0001:
                print('p-value: <0.0001')
            else:
                print(f'p-value: {round(p,4)}')
            fig, axes = plt.subplots(1, 2, figsize=(10, 4))
            cross_tab.plot(kind='bar', stacked=False,width=0.9, ax=axes[0])
            d = proportions.plot(kind = 'bar',ax=axes[1])
            d.bar_label(d.containers[0])
            plt.title(f'Proportion of {j}={cross_tab.columns[1]} vs {i}')
            plt.show()

#%%
# Calling the function
cat_c = ['avg_220', 'avg_240', 'avg_260',
       'avg_280', 'avg_300', 'hr_10', 'hr_20', 'hr_30', 'hr_40', 'sb_05',
       'sb_10', 'sb_15', 'sb_20']

cat_bivariate(bat_22_23,['year'], cat_c)

#%%
# Alternative method: Mosaic plots from statsmodel
from statsmodels.graphics.mosaicplot import mosaic
cat_c = ['avg_220', 'avg_240', 'avg_260',
       'avg_280', 'avg_300', 'hr_10', 'hr_20', 'hr_30', 'hr_40', 'sb_05',
       'sb_10', 'sb_15', 'sb_20']
for x in cat_c:
    mosaic(bat_22_23, ['year',x])
    plt.show()
