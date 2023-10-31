#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:52:28 2023

@author: danielferreira
"""

folder = '/Users/danielferreira/Documents/repositories/pySTETV/06 - Utility & References/Data'
file = 'player_batting_enriched.csv'

#%%
# What is the size of the file (if the data is in a file system)?
import os
os.chdir(folder)
size = os.path.getsize(file)
print(f'The Size of your file is: {round(size/1024,2)} kb or {round(size/1024**2,2)} mb or {round(size/1024**3,2)} gb')

#%%
# How columns are delimited?
# First row contains columns names?
with open(file,'r') as temp_rows:
    temp=temp_rows.readline()
    print('First Row:\n')
    print(temp)
    temp=temp_rows.readline() 
    print('Second Row:\n')
    print(temp)

#%%
# Now we can import the data:
import pandas as pd
bat = pd.read_csv(file)

#%%
# How many rows and columns?
print(f'{bat.shape[0]} rows and {bat.shape[1]} columns.')
# You can also only use:
bat.shape

#%%
# What are the name of the columns?
bat.columns

#%%
# How the first rows look like?
bat.head() # Looks better on jupyter notebook
