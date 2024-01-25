#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 18:32:31 2024

@author: danielferreira
"""

# Pre-Process
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier, HistGradientBoostingClassifier
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
# Defaul AdaBoost
model1 = AdaBoostClassifier()
model1.fit(X_train, y_train)
y_pred = model1.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# You can change the estimator, by defaul it uses stumps (DecisionTreeClassifier(max_depth=1))
from sklearn.linear_model import LogisticRegression
model2 = AdaBoostClassifier(estimator=LogisticRegression())
model2.fit(X_train, y_train)
y_pred = model2.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# Learning Rates and max number of estimators can be tweaked for simpler or more complex models
model4 = AdaBoostClassifier(learning_rate = 1.5, n_estimators = 20) # Simpler Model
model4.fit(X_train, y_train)
y_pred = model4.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# Default Gradient Boosting Classifier
model5 = GradientBoostingClassifier()
model5.fit(X_train, y_train)
y_pred = model5.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# This table is small, but for larger tables Histogram based GB can work faster
model6 = HistGradientBoostingClassifier()
model6.fit(X_train, y_train)
y_pred = model6.predict(X_test)
accuracy_score(y_test, y_pred)

#%%
# You can find more in the official sklearn.ensemble documentation: https://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble

