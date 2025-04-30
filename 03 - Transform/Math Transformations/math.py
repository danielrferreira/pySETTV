#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:39:51 2023

@author: danielferreira
"""

#%%
# Common math transformations

#%%

#%%
# Import libs and data
import numpy as np
from scipy.stats import boxcox
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
index = 'player_id'
os.chdir(folder)
bat = pd.read_csv(file, index_col=index)

#%%
# log (x)
# Purpose: Reduces the impact of outliers and scales down large values.
bat['ln_ab'] = np.log(bat['ab'])
bat[['ab','ln_ab']].head()

#%%
# log (x+1)
# Purpose: Reduces the impact of outliers, scales down large values and avoid log(0).
bat['ln_ab'] = np.log(bat['ab']+1)
bat[['ab','ln_ab']].head()

#%%
# sqrt
# Purpose: Similar to the logarithmic transformation, reduces the impact of large values.
old_name = 'player_age'
new_name = 'player_age_sqrt'
bat[new_name] = np.sqrt(bat[old_name])
bat[[old_name,new_name]].head()

#%%
# Square
# Purpose: Highlights differences among small values.
old_name = 'player_age'
new_name = 'player_age_sqrd'
bat[new_name] = bat[old_name]**2
bat[[old_name,new_name]].head()

#%%
# Box-Cox
# If you are trying to make the data look like normal, and your data is positive, you can also use box-cox. 
# boxcox will find the optimal parameter of the transformation maximizing the likelihood of the transformed data under normal distribution assumption
old_name = 'player_age'
new_name = 'player_age_bc'
bat[new_name] , lambda_parameter = boxcox(bat[old_name])
plt.hist(bat[new_name])
plt.title(f'Box-Cox Transformation of {old_name}. Lambda = {round(lambda_parameter,4)}.')

#%%
# If you want to apply the same transformation to many columns, you can create a function and use it on a loop
def log_x_plus_1(x):
    return np.log(x+1)
col_log = ['player_age', 'ab', 'home_run', 'batting_avg']
for x in col_log:    
    bat[x+'_log']= log_x_plus_1(bat[x])
bat[['player_age', 'ab', 'home_run', 'batting_avg','player_age_log', 'ab_log', 'home_run_log', 'batting_avg_log']].head()

#%%
# When trying to apply the best transformation, we usually like to see histograms before and after. 
# This function can try multiple transformation and plot it against original
import numpy as np
from scipy.stats import boxcox
import matplotlib.pyplot as plt
import seaborn as sns

def log_x_plus_1(x):
    return np.log(x+1), 'Log(X+1)'
    
def square_root(x):
    return np.sqrt(x), 'SQRT(X)'
    
def squared(x):
    return x**2, 'X^2'
    
def boxcox_auto(x):
    transf_values , lambda_parameter = boxcox(x)
    title = f'Box-Cox(X) Lambda={round(lambda_parameter,2)}'
    return transf_values, title
    
def winsoring(x):
    return np.minimum(x,x.quantile(0.99)), 'Winsoring'
    
def multi_transf(data, columns, transf=[log_x_plus_1,boxcox_auto, winsoring], scale_graph=9, aspect_ratio=2/3):
    '''Create multiple Histograms plots with original and trasformed columns  
    Args:
        data: Input data-frame containing variables we wish to plot.
        columns: Listing of column-names we wish to plot.
        transf: List of methods we wish to apply to original plot. Possible methods: log_x_plus_1, square_root, squared, boxcox_auto, winsoring
        scale_graph: Adjust the total size of the graph.
        aspect_ratio: Adjust the aspect ratio of each individual graph. For squared graphs use 1/1.
    '''   
    # Adjusting how many rows and columns the grid will have and proper sizes
    n_cols = len(transf)+1
    n_rows = len(columns)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(scale_graph, (scale_graph/n_cols)*aspect_ratio*n_rows))
    # Plot
    for i, x in enumerate(columns):
        sns.histplot(data=data[x],ax=axes[i,0], kde=True)
        axes[i,0].set_title(x)
        for j, func in enumerate(transf):
            if (data[x].min()<=0) & (func==boxcox_auto):
                axes[i,j+1].set_title('Box-Cox not possible')
                print(f'Box-Cox not computed for {x}, non-positive values')
            else:
                transf_data, tle = func(data[x])
                sns.histplot(data=transf_data ,ax=axes[i,j+1], kde=True)
                axes[i,j+1].set_title(tle)
    plt.tight_layout()

#%%
# Calling the function
num_c = ['player_age', 'ab', 'single', 'batting_avg', 'slg_percent']
multi_transf(bat, num_c)

#%%
# You can change the transformations
num_c = ['player_age', 'ab']
multi_transf(bat, num_c, transf=[squared, square_root, log_x_plus_1])
