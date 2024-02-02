#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:45:52 2024

@author: danielferreira
"""

# Pre process
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import os
folder = '/Users/danielferreira/Documents/repositories/pySETTV/06 - Utility & References/Data'
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
# For distance-based algorithms is always a good idea to standardize your data:
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

#%%
# Default KNN
model1 = KNeighborsClassifier()
model1.fit(X_train, y_train)
y_pred = model1.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# By default, k=5. By increasing K, you reduces the chance of overfitting. Usually use odd numbers to avoid ties.
model2 = KNeighborsClassifier(n_neighbors=13)
model2.fit(X_train, y_train)
y_pred = model2.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# This code can help see how k impacts accuracy:
acc_df = pd.DataFrame({'k':[] , 'asc':[]})
Ks = np.arange(3,27,2)
for k in Ks:
    model3= KNeighborsClassifier(n_neighbors=k)
    model3.fit(X_train, y_train)
    y_pred = model3.predict(X_test)
    asc = accuracy_score(y_test, y_pred)
    temp_df = pd.DataFrame({'k':[k] , 'asc':[asc]})
    acc_df = pd.concat([acc_df, temp_df])
plt.plot(acc_df['k'], acc_df['asc'], marker='o')
plt.show()
# PS1.: It doesn't make sense to use test data to decide the best k, we might need a validation data set, or cross validation
# PS2.: Accuracy is also not the best metric, since is not very sensitive

#%%
# Metric and p controls how similarity is calculated. default is Euclidean Distance (minkowski with p=2)
model4 = KNeighborsClassifier(metric='cityblock')
model4.fit(X_train, y_train)
y_pred = model4.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# To calculate the neighbors, there are alternatives to brute force, such as balltree algorithm. The default is auto, it decides the algorithm based on your inputs
model5 = KNeighborsClassifier(algorithm = 'ball_tree')
model5.fit(X_train, y_train)
y_pred = model5.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# An alternative to KNN is Radius Neighbors. This method uses the neighbors whitin a radius from the data point you are trying to classify.
from sklearn.neighbors import RadiusNeighborsClassifier
model6 = RadiusNeighborsClassifier(radius=0.5)
model6.fit(X_train, y_train)
y_pred = model6.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# radius controls how far we go to collect the neighbors to avoid overfitting.
acc_df = pd.DataFrame({'r':[] , 'asc':[]})
Rs = np.arange(0.5,3,0.1)
for r in Rs:
    model7= RadiusNeighborsClassifier(radius=r)
    model7.fit(X_train, y_train)
    y_pred = model7.predict(X_test)
    asc = accuracy_score(y_test, y_pred)
    temp_df = pd.DataFrame({'r':[r] , 'asc':[asc]})
    acc_df = pd.concat([acc_df, temp_df])
plt.plot(acc_df['r'], acc_df['asc'], marker='o')
plt.show()
