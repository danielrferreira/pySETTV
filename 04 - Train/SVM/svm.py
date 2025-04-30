#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:00:03 2024

@author: danielferreira
"""

# Pre-Process
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import os
folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
index = 'player_id'
os.chdir(folder)
bat = pd.read_csv(file, index_col=index)
train = bat[bat['year']==2021]
test = bat[bat['year']==2022]
y_train = train['hr_10'].copy()
X_train = train[['ab','exit_velocity_avg', 'batting_avg','r_total_stolen_base']].copy()
X_train['exit_velocity_avg'] = X_train['exit_velocity_avg'].fillna(X_train['exit_velocity_avg'].median())
y_test = test['hr_10'].copy()
X_test = test[['ab','exit_velocity_avg', 'batting_avg','r_total_stolen_base']].copy()
X_test['exit_velocity_avg'] = X_test['exit_velocity_avg'].fillna(X_test['exit_velocity_avg'].median())

#%%
# Default SVM
model1 = SVC()
model1.fit(X_train, y_train)
y_pred = model1.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# Simpler SVM using linear kernel. (No "move to higher dimensions" step)
model2 = SVC(kernel='linear')
model2.fit(X_train, y_train)
y_pred = model2.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# Since the last model performed better, it seems RFB kernel (default kernel) is an overkill, let's try to change C to make an even simpler model
model3= SVC(kernel='linear', C=0.2)
model3.fit(X_train, y_train)
y_pred = model3.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# This code can help see how c impacts accuracy:
acc_df = pd.DataFrame({'c':[0.1] , 'asc':[0.8726708074534162]})
Cs = np.arange(0.2,2,0.1)
for c in Cs:
    model3= SVC(kernel='linear', C=c)
    model3.fit(X_train, y_train)
    y_pred = model3.predict(X_test)
    asc = accuracy_score(y_test, y_pred)
    temp_df = pd.DataFrame({'c':[c] , 'asc':[asc]})
    acc_df = pd.concat([acc_df, temp_df])
plt.plot(acc_df['c'], acc_df['asc'], marker='o')
# PS1.: It doesn't make sense to use test data to decide the best C, we might need a validation data set
# PS2.: Accuracy is also not the best metric, since is not very sensitive
# PS3: Don't do that with big data sets, it might take a while for the computer to proccess

#%%
# For polynomial Kernel, we can also decide the degree of the polynomial
model4= SVC(kernel='poly', degree=2)
model4.fit(X_train, y_train)
y_pred = model4.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# SVM are a classification algorithm, if you need probabilites you need to ask for it:
model5 = SVC(kernel='linear', C=1, probability=True)
model5.fit(X_train, y_train)
y_pred = model5.predict(X_test)
accuracy_score(y_test, y_pred)
