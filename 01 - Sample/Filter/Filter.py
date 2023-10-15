#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:18:24 2023

@author: danielferreira
"""
# Filter data examples

import pandas as pd
from os import chdir

chdir('/Users/danielferreira/Documents/repositories/pySTETV/06 - Utility & References/Data')
batting_all = pd.read_csv('batting_2021_2022_2023.csv')
print(batting_all.shape)
print(batting_all.columns)
batting_all.head()

#%%
# To Filter columns we can use lists, and then reference then as indexes
columns_to_keep = ['last_name, first_name', 'player_age',
                   'year', 'exit_velocity_avg', 'batting_avg']
bb_subset = batting_all[columns_to_keep]
bb_subset.head()

#%%
# An alternative would be to use drop method with axis=1 to remove columns
bb_subset = bb_subset.drop('exit_velocity_avg', axis=1)

#%%
# To filter rows, the easiest way is to provide a boolean Series with the same size of the table
bb_2023 = bb_subset[bb_subset['year']==2023]  # Note that bb_subset['year']==2023 returns a boolean Series with the same size as len(bb_subset)
# You can combine drop with the filter to remove redundant columns:
bb_2023 = (bb_subset[bb_subset['year']==2023]).drop('year', axis=1)

#%%
# We can use logical operators and other methods
consistent = bb_2023[ (bb_2023['player_age']>30) & (bb_2023['batting_avg']>0.250) ]
print(consistent)

#%%
# As an alternative, we can use loc and iloc methods to filter using labels or interger positions:

# iloc uses the integer index of rows or columns, first argument is rows and second is columns
sorted_2023 = consistent.sort_values(by='batting_avg', ascending=False) # Sort not needed, just doing to make the filter below make sense.
top5 = sorted_2023.iloc[0:5]
top5_names = sorted_2023.iloc[0:5,0]

# loc can be usefull if you are trying to filter based on index, or filtering rows and columns
good_average = bb_2023.loc[bb_2023['batting_avg']>0.250, ['last_name, first_name','batting_avg']]

#%%
# Just out of curiosity
top10last3years = (bb_subset.sort_values(by='batting_avg', ascending=False)).iloc[0:10]
