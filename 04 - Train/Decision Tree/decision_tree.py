#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 18:24:45 2024

@author: danielferreira
"""

# Pre-Process
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
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
# Fit and Predict follows the same idea as any other sklearn method
model1 = DecisionTreeClassifier()
model1.fit(X_train, y_train)
pred_test = model1.predict(X_test)
accuracy_score(pred_test, y_test)

#%%
# Plotting the tree
plt.figure(figsize=(12, 8))
plot_tree(model1, feature_names=list(X_train.columns), class_names=['<10','>=10'])
plt.show()

#%%
# Many times the trees are too big to be plotted. Seeing the rules as texts may help
tree_rules = export_text(model1, feature_names=list(X_train.columns))
print(tree_rules)

#%%
### To avoid overfitting, we can use the following parameters:
# - Limiting Tree Depth (max_depth): Set the maximum depth of the tree. A shallower tree is less likely to overfit.
# - Minimum Samples for a Split (min_samples_split): Specify the minimum number of samples required to split an internal node. Increasing this parameter can prevent the model from creating splits that capture noise.
# - Minimum Samples in a Leaf Node (min_samples_leaf): Define the minimum number of samples required to be in a leaf node. This helps control the size of the leaves and can prevent overfitting.
# - Maximum Features (max_features): Limit the number of features considered for a split. This can be particularly useful when dealing with a large number of features.

#%%
# Simpler Decision Tree (Pruned)
model2 = DecisionTreeClassifier(max_depth=3, min_samples_split=30, min_samples_leaf = 20, max_features=3)
model2.fit(X_train, y_train)
pred_test = model2.predict(X_test)
accuracy_score(pred_test, y_test)

#%%
# Simple DT Plot
plt.figure(figsize=(12, 8))
plot_tree(model2, feature_names=list(X_train.columns), class_names=['<10','>=10'])
plt.show()
