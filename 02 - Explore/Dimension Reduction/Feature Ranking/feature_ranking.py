#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:40:18 2023

@author: danielferreira
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import os
folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
os.chdir(folder)
bat = pd.read_csv(file)
cat_c = ['avg_220', 'avg_240', 'avg_260',
       'avg_280', 'avg_300', 'hr_20', 'hr_30', 'hr_40', 'sb_05',
       'sb_10', 'sb_15', 'sb_20']
num_c = ['player_age', 'ab', 'pa', 'hit', 'single',
       'double', 'triple', 'home_run', 'strikeout', 'walk', 'k_percent',
       'bb_percent', 'slg_percent', 'on_base_percent',
       'on_base_plus_slg', 'b_rbi', 'r_total_caught_stealing',
       'r_total_stolen_base', 'exit_velocity_avg', 'sweet_spot_percent',
       'barrel_batted_rate', 'hp_to_1b', 'sprint_speed']
outcome_cat = ['hr_10']
outcome_num = ['batting_avg']

#%%
# For categorical vs categorical we can use -log of Chi-Square tests to rank variables
def log_worth(data,col1,col2):
    '''Calculate -log of p-value of Chi-Square tests for any combination of categorigal variables. 
    
    Args:
        data: Data Frame
        col1: List of input categorical columns
        col2: List of outcome variables
    '''
    int = 0
    var_rank = pd.DataFrame({'var1':'mu','var2':'mu','chi2':1.1,'p_value':1.1,'log_worth':1.1},index=[int])
    for i in col1:
        for j in col2:
            int += 1
            cross_tab = pd.crosstab(data[i], data[j])
            chi2, p = chi2_contingency(cross_tab)[0:2]
            lw = -np.log(p)
            temp1 = pd.DataFrame({'var1':i,'var2':j,'chi2':chi2,'p_value':p,'log_worth':lw},index=[int])
            var_rank = pd.concat([var_rank,temp1])
    var_rank = var_rank[var_rank.index!=0]
    var_rank = var_rank.sort_values('log_worth',ascending=False)
    print(var_rank)
    for i in col1:
        temp2 = var_rank[var_rank['var1']==i]
        temp2 = temp2.sort_values('log_worth',ascending=True)
        temp2[['var2','log_worth']].plot(kind='barh', x = 'var2', title=f'Log Worth {i} vs other variables')
        
#%%
# Calling the function
log_worth(bat, outcome_cat, cat_c)

#%%
# For numerical columns we will use correlation (Pearson or Spearman)
def corr_graph(data,outcome,x_columns,c_method='pearson'):
    '''
    This function plots all the absolute correlations in a bar chart.
    Args:
        data: Input data-frame.
        outcome: Numerical variable that we will use to calculate correlations.
        x_columns: Listing of column-names we wish to correlate with outcome.
        c_method: Correlation Formula used ('pearson', 'kendall', 'spearman')
    '''
    c = data[x_columns].corrwith(data[outcome],method=c_method)
    abs_c = abs(c)
    colors = pd.Series(['blue' if val > 0 else 'red' for val in c],index=c.index)
    corr_df = pd.DataFrame([c,abs_c,colors],index=['correlation','absolute_corr','color']).T.sort_values('absolute_corr')
    corr_df.plot(kind='barh', y='absolute_corr', color=corr_df['color'], legend=False)
    plt.xlabel('Absolute Correlation')
    plt.ylabel('Features')
    plt.title('Correlations (Blue is positive, Red is Negative)')
    plt.show()

#%%
# Calling the function
corr_graph(bat,'batting_avg', num_c, c_method='spearman')

#%%
# Random Forest have impurity-based feature importances. The higher, the more important the feature. The importance of a feature is computed as the (normalized) total reduction of the criterion brought by that feature. It is also known as the Gini importance.
from sklearn.ensemble import RandomForestClassifier

all_c = [ 'sb_05',
         'sb_10', 'sb_15', 'sb_20', 'player_age', 'ab', 'pa', 'hit', 'single',
         'double', 'triple', 'strikeout', 'walk', 'k_percent',
         'bb_percent', 'slg_percent', 'on_base_percent',
         'on_base_plus_slg', 'b_rbi', 'r_total_caught_stealing',
         'r_total_stolen_base', 'sweet_spot_percent',
         'barrel_batted_rate']
X = bat[all_c]
y = bat['avg_240']
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)
feature_importances = pd.Series(rf_model.feature_importances_, index=rf_model.feature_names_in_)
feature_importances = feature_importances.sort_values()
plt.barh(range(X.shape[1]), feature_importances)
plt.yticks(range(X.shape[1]),feature_importances.index )
plt.xlabel('Feature Importance')
plt.ylabel('Feature Name')
plt.title('Random Forest Variable Importance')
plt.show()
