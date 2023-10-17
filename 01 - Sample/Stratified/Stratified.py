#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:19:42 2023

@author: danielferreira
"""

from os import chdir
chdir('/Users/danielferreira/Documents/repositories/pySTETV/01 - Sample/Stratified')
import pandas as pd
baseball = pd.read_csv('batting_2021_2022_2023.csv')

#%%
# To sample using strata variables we can use groupby method to later call sample method using apply and a lambda function
sample_size = 10
stratified_sample = baseball.groupby('year', group_keys=False).apply(lambda x: x.sample(min(len(x), sample_size)))

#%%
# To balance a sample we can just change the size of the sample to be equal as the number of rare events (usually the 1's)
# Ignore this manipulation, it just create a flag variable to use as binary outcome
baseball['y'] = baseball['batting_avg']>0.3
# Find the number of observations from the rare event:
sample_size = baseball['y'].sum()
print(sample_size)
# Sample all positive cases, and the same number of negative cases
balanced_sample = baseball.groupby('y', group_keys=False).apply(lambda x: x.sample(sample_size))

#%%
# If you want to stratify your data partition, you can use directly train_test_split from sklearn with stratify argument
from sklearn.model_selection import train_test_split
y = baseball['y']
X = baseball.drop('y', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=19, stratify=X['year'])
print('Distribution of year in Train')
print(X_train['year'].value_counts(normalize=True))
print('Distribution of year in Test')
print(X_test['year'].value_counts(normalize=True))

#%%
# If you want to see how that would be without strata variable you can run this code:
y = baseball['y']
X = baseball.drop('y', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=19)
print('Distribution of year in Train')
print(X_train['year'].value_counts(normalize=True))
print('Distribution of year in Test')
print(X_test['year'].value_counts(normalize=True))
