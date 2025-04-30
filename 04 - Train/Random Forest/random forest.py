#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:35:29 2024

@author: danielferreira
"""

# Pre-Process
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
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
# Simple Decision Tree 
model1 = DecisionTreeClassifier(max_depth=3, min_samples_split=30, min_samples_leaf = 20, max_features=3)
model1.fit(X_train, y_train)
pred_test = model1.predict(X_test)
print(accuracy_score(pred_test, y_test))
plt.figure(figsize=(12, 8))
plot_tree(model1, feature_names=list(X_train.columns), class_names=['<10','>=10'])
plt.show()

#%%
# Default Random Forest
model2 = RandomForestClassifier(random_state=42)
model2.fit(X_train,y_train)
pred_test = model2.predict(X_test)
accuracy_score(pred_test, y_test)

#%%
# n_estimators:
#    - Description: The number of trees in the forest.
#    - Default: 100
# criterion:
#   - Description: The function to measure the quality of a split. "gini" for Gini impurity or "entropy" for information gain.
#    - Default: "gini"
# max_depth:
#    - Description: The maximum depth of the tree. If None, the nodes are expanded until all leaves are pure or until they contain less than min_samples_split samples.
#    - Default: None
# min_samples_split:
#    - Description: The minimum number of samples required to split an internal node.
#    - Default: 2
# min_samples_leaf:
#    - Description: The minimum number of samples required to be at a leaf node.
#    - Default: 1
# max_features:
#    - Description: The number of features to consider when looking for the best split.
#    - Default: "auto" (sqrt(n_features))
# min_impurity_decrease:
#   - Description: A node will be split if this split induces a decrease of the impurity greater than or equal to this value.
#   - Default: 0.0
# random_state:
#   - Description: If int, random_state is the seed used by the random number generator.
#   - Default: None

#%%
# Default Entropy Random Forest
model3 = RandomForestClassifier(random_state=42,criterion='entropy' )
model3.fit(X_train,y_train)
pred_test = model3.predict(X_test)
accuracy_score(pred_test, y_test)

#%%
# Combine a larger number of simpler trees
model4 = RandomForestClassifier(random_state=42, n_estimators = 2000, max_depth=3, min_samples_split=30, min_samples_leaf = 20, max_features=3)
model4.fit(X_train,y_train)
pred_test = model4.predict(X_test)
accuracy_score(pred_test, y_test)

#%%
# Random Forest have impurity-based feature importances. The higher, the more important the feature. So it can be used to rank features
y = train['hr_10'].copy()
rank_cols = ['player_age', 'ab', 'pa', 'hit', 'single', 'double',
       'triple', 'strikeout', 'walk', 'k_percent', 'bb_percent',
       'batting_avg', 'slg_percent', 'on_base_percent', 'on_base_plus_slg',
       'b_rbi', 'r_total_caught_stealing', 'r_total_stolen_base',
       'sweet_spot_percent', 'barrel_batted_rate']
X = train[rank_cols]
rank_model = RandomForestClassifier(n_estimators=100, random_state=42)
rank_model.fit(X, y)
feature_importances = pd.Series(rank_model.feature_importances_, index=rank_model.feature_names_in_)
feature_importances = feature_importances.sort_values()
plt.barh(range(X.shape[1]), feature_importances)
plt.yticks(range(X.shape[1]),feature_importances.index )
plt.xlabel('Feature Importance')
plt.ylabel('Feature Name')
plt.title('Random Forest Variable Importance')
plt.show()
