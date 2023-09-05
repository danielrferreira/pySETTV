#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:26:12 2023

@author: danielferreira
"""

#%%
# This function splits the data into Train/Validation/Test. This code used pandas sample method. If you need something faster I encourage you to change the code and use NumPy random module instead.
def data_partition(data, train_ratio=0.5, val_ratio=0.5, test_ratio=0, seed=420):
    '''This function splits the data into train, validation and test, it return 2 data frames if test_ratio=0 or 3 data frames if test_ratio>0'''
    data_shuffle = data.sample(frac=1, random_state=seed).reset_index(drop=True)
    if test_ratio==0:
        train_size = int(train_ratio * len(data))
        val_size = len(data) - train_size
        print(f'Two splits created. Train ({train_size} observations and Validation ({val_size} observations.')
        return data_shuffle[:train_size],data_shuffle[train_size:train_size + val_size]
    else:
        train_size = int(train_ratio * len(data))
        val_size = int(val_ratio * len(data))
        test_size = len(data) - train_size - val_size
        print(f'Three splits created. Train ({train_size} observations), Validation ({val_size} observations) and test ({test_size}).')
        return data_shuffle[:train_size], data_shuffle[train_size:train_size + val_size], data_shuffle[train_size + val_size:]

#%%
# Examples
import pandas as pd
baseball = pd.read_csv('/Users/danielferreira/Documents/repositories/pySTETV/Sample/Data Partition/baseball_stats_batting_2020_2023.csv')

#%%
# For 50/50 Train/Validation
bb_train, bb_val = data_partition(baseball) 

#%%
# For 50/50 Train/Validation, different seed
bb_train, bb_val = data_partition(baseball,seed=12345)

#%%
#For 70/30 Train/Validation
bb_train, bb_val = data_partition(baseball,train_ratio=0.7,val_ratio=0.3) 

#%%
#0.7/0.15/0.15 T/V/T
bb_train, bb_val, bb_test = data_partition(baseball,train_ratio=0.7,val_ratio=0.15,test_ratio=0.15) 
