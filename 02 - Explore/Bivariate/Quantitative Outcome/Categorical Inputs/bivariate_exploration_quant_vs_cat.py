#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:11:03 2023

@author: danielferreira
"""

# Import modules and data set
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
folder = '/Users/danielferreira/Documents/repositories/pySETTV/06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
os.chdir(folder)
bat = pd.read_csv(file)

#%%
# For low cardinality inputs, we can use Kernel Distribution can help check if the variable has association with the outcome
outcome =  'batting_avg'
x = 'hr_10'
data = bat
plt.title(f'Distribution of {outcome} by {x}') 
sns.kdeplot(data=data, x=outcome, hue=x, common_norm=False)
plt.show

#%%
# This function do the above for a list of x variables
def kernel_plots(data, outcome, x_columns, scale_graph=9, n_cols=3, aspect_ratio=2/3 ):
    '''Create multiple kernel plots using a subset of variables specified.
    
    Args:
        data: Input data-frame.
        outcome: Numerical variable.
        x_columns: Listing of column-names we wish to plot against outcome.
        scale_graph: Adjust the total size of the graph.
        n_cols: Adjust how many graphs we have on each row.
        aspect_ratio: Adjust the aspect ratio of each individual graph. For squared graphs use 1/1.
    '''

    # Adjusting how many rows the grid will have and proper sizes
    n_rows = len(x_columns)//n_cols+(len(x_columns)%n_cols>0) 
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(scale_graph, (scale_graph/n_cols)*aspect_ratio*n_rows))

    # Plotting
    fig.suptitle(f'Kernel Dists of {len(x_columns)} columns by {outcome}',y=1, size=15)
    axes=axes.flatten()
    for i,feature in enumerate(x_columns):
        sns.kdeplot(data=data, ax=axes[i], x=outcome, hue=feature, common_norm=False)
    plt.tight_layout()

#%%
# Calling the function
cat_c = ['hr_10','sb_05', 'sb_10']
kernel_plots(bat, 'batting_avg', cat_c )

#%%
# Another option is to use violin plots
plt.title(f'Distribution of {outcome} by {x}') 
sns.violinplot(data=data, y=outcome, x=x)
plt.show

#%%
# Function to get the above for a list of variables
def violin_plots(data, outcome, x_columns, scale_graph=9, n_cols=3, aspect_ratio=2/3 ):
    '''Create multiple violin plots by a categorical variable.
    
    Args:
        data: Input data-frame.
        outcome: Categorical variable that we will use as hue.
        x_columns: Listing of column-names we wish to plot against outcome.
        scale_graph: Adjust the total size of the graph.
        n_cols: Adjust how many graphs we have on each row.
        aspect_ratio: Adjust the aspect ratio of each individual graph. For squared graphs use 1/1.
    '''

    # Adjusting how many rows the grid will have and proper sizes
    n_rows = len(x_columns)//n_cols+(len(x_columns)%n_cols>0) 
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(scale_graph, (scale_graph/n_cols)*aspect_ratio*n_rows))

    # Plotting
    fig.suptitle(f'Violin plots of {len(x_columns)} columns by {outcome}',y=1, size=15)
    axes=axes.flatten()
    for i,feature in enumerate(x_columns):
        sns.violinplot(data=data, ax=axes[i],y=outcome, x=feature)
    plt.tight_layout()

#%%
# Calling the function
violin_plots(bat, 'batting_avg', cat_c )
