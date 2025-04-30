#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:12:28 2023

@author: danielferreira
"""

# Importing Data Set for our examples:
folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
import os
import pandas as pd
os.chdir(folder)
bat = pd.read_csv(file)

#%%
# First thing is to calculate the number of missings by columns:
missings = bat.isna().sum()
print(missings)
# If you want in percentage:
missings = bat.isna().sum() / len(bat)
print(missings)

#%%
# You can also use seaborn to visualize the distribution of missings
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(missings, bw_adjust=0.1)
plt.suptitle("Distribution of missing values in each column")

#%%
# If you want to look only at columns with more than 0 missings (or any other threshold):
missings[missings>0]

#%%
# If you  want to understand if multiple columns have missings in the same rows:
bat[bat['team_id'].isna()]['team_name'].isna().sum()/len(bat[bat['team_id'].isna()])
# We can also build a loop to have pairwise missing reports
