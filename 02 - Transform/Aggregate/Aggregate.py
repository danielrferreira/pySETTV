#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 09:11:50 2023

@author: danielferreira
"""

# You can ignore this next part
from os import chdir
chdir('/Users/danielferreira/Documents/repositories/pySTETV/02 - Transform/Aggregate')
import pandas as pd
baseball = pd.read_csv('batting_2021_2022_2023.csv', index_col='player_id')

#%%
# Aggregate can be done using groupby
avg_batting_year = baseball.groupby('year')['batting_avg'].mean() # Series with year as index
avg_batting_year_df = baseball.groupby('year')['batting_avg'].mean().reset_index() # DataFrame
hr_player = baseball.groupby('name')['home_run'].sum().reset_index()

#%%
# Methods for aggregattion:
# count, sum, mean, min, max
# quantile, median
# argmin, argmax, idxmin, idxmax: Index of Min and Maximum, arg returns integer, idx returns label.
# std, var, skew, kurt
# cumsum and many others, see pandas documentation for all.

#%%
# Alternative
