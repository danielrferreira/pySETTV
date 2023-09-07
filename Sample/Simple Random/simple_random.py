#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:19:42 2023

@author: danielferreira
"""

# Sample Function
def sample(data_in,mode='percent',size_smp=0.2,repl=False,seed_smp=None):
    '''This function has two modes, percent and n. The first returns a sample given a percentage (mode='percent', size_smp=0.2), the second returns a sample with a specific n (mode='n', size_smp=1000)'''
    import numpy as np
    if (mode=='n' and size_smp>len(data_in)):
        print('Sample Size is greater than data frame provided. Function Aborted')
    else:
        if seed_smp != None:
            start_point = np.random.default_rng(seed=seed_smp)
            print(f'Seed fixed = {seed_smp}')
            if mode=='percent':
                sample_size=int(size_smp * len(data_in))
                indices = start_point.choice(data_in.index, size=sample_size, replace=repl)
                print(f'Sample has {sample_size} observations') 
                return data_in.loc[indices]
            if mode=='n':
                indices = start_point.choice(data_in.index, size=size_smp, replace=repl)
                print(f'Sample has {size_smp} observations') 
                return data_in.loc[indices]
        else:
            if mode=='percent':
                sample_size=int(size_smp * len(data_in))
                indices = np.random.choice(data_in.index, size=sample_size, replace=repl)
                print(f'Sample has {sample_size} observations') 
                return data_in.loc[indices]
            if mode=='n':
                indices = np.random.choice(data_in.index, size=size_smp, replace=repl)
                print(f'Sample has {size_smp} observations') 
                return data_in.loc[indices]
            
#%%
# Examples:
import pandas as pd
baseball = pd.read_csv('/Users/danielferreira/Documents/repositories/pySTETV/Sample/Data Partition/baseball_stats_batting_2020_2023.csv')

#%%
# Simple 20% sample using arbitrary seed. It will return a different sample everytime you run.
bb_sample = sample(baseball)

#%%
# Changing seed.
bb_sample = sample(baseball,seed_smp=420)

#%%
# Using mode 'n'.
bb_sample = sample(baseball,mode='n',size_smp=1200)

#%%
# Using sample size greater than size of the data frame. It will print a message.
bb_sample = sample(baseball,mode='n',size_smp=1800)
