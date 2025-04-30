#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:34:37 2024

@author: danielferreira
"""

# Pre process
import pandas as pd
import os
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
from sklearn.metrics import accuracy_score, classification_report
folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
index = 'player_id'
os.chdir(folder)
bat = pd.read_csv(file, index_col=index)
train = bat[bat['year']==2021]
test = bat[bat['year']==2022]
y_train = train['hr_10'].copy()
y_test = test['hr_10'].copy()

#%%
# Multinominal variables
X_train = train[['league','division', 'avg_220','triple']].copy()
X_test = test[['league','division', 'avg_220','triple']].copy()
one_hot = ['division','league']
X_train = pd.get_dummies(data=X_train, columns=one_hot, drop_first=True)
X_test = pd.get_dummies(data=X_test, columns=one_hot, drop_first=True)

#%%
# Multinominal Naive Bayes
model1 = MultinomialNB()
model1.fit(X_train, y_train)
y_pred = model1.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# Binary only
X_train = train[['league','division', 'avg_220']].copy()
X_test = test[['league','division', 'avg_220']].copy()
one_hot = ['division','league']
X_train = pd.get_dummies(data=X_train, columns=one_hot, drop_first=True)
X_test = pd.get_dummies(data=X_test, columns=one_hot, drop_first=True)

#%%
# For binary/boolean only inputs, you may want to prefer BernoulliNB
model2 = BernoulliNB()
model2.fit(X_train, y_train)
y_pred = model2.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# Quantitative Variables Only
X_train = train[['k_percent', 'bb_percent','batting_avg', 'slg_percent']].copy()
X_test = test[['k_percent', 'bb_percent','batting_avg', 'slg_percent']].copy()

#%%
# Gaussian
model3 = GaussianNB()
model3.fit(X_train, y_train)
y_pred = model3.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# Since the accuracy is low and our outcome has 30% of True's, seeing what is happening in detail can help. 
print(classification_report(y_test, y_pred, target_names = ['>=10','<10']))
