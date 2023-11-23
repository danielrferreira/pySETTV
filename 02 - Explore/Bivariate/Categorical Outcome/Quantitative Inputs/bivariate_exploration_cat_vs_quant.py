#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:11:03 2023

@author: danielferreira
"""

# Import modules and data set
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
folder = '/Users/danielferreira/Documents/repositories/pySETTV/06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
os.chdir(folder)
bat = pd.read_csv(file)

#%%
# Kernel Distribution can help check if the variable has association with the outcome
outcome =  'hr_10'
x = 'batting_avg'
data = bat
plt.title(f'Distribution of {outcome} by {x}') 
sns.kdeplot(data=data, x=x, hue=outcome, common_norm=False)
plt.show

#%%
# This function do the above for a list of x variables
def kernel_plots(data, outcome, x_columns, scale_graph=9, n_cols=3, aspect_ratio=2/3 ):
    '''Create multiple kernel plots using a subset of variables specified.
    
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
    fig.suptitle(f'Kernel Dists of {len(x_columns)} columns by {outcome}',y=1, size=15)
    axes=axes.flatten()
    for i,feature in enumerate(x_columns):
        sns.kdeplot(data=data, ax=axes[i], x=feature, hue=outcome, common_norm=False)
    plt.tight_layout()

#%%
# Calling the function
num_c = ['player_age', 'batting_avg', 'sweet_spot_percent', 'on_base_percent', 'strikeout', 'sprint_speed']
kernel_plots(bat, 'hr_10', num_c )

#%%
# Another option is to use violin plots
plt.title(f'Distribution of {outcome} by {x}') 
sns.violinplot(data=data, y=x, x=outcome)
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
        sns.violinplot(data=data, ax=axes[i],y=feature, x=outcome)
    plt.tight_layout()

#%%
# Calling the function
violin_plots(bat, 'hr_10', num_c )

#%%
# For Logistic Regresssions, it is a good idea to plot ln(p/1-p) vs different ranges of the numerical column, this would help us to understand if transformations are needed or if the numerical variable has something close to a linear relationship with the transformed outcome (ln(p/1-p).
def ln_analysis(data, outcome, x_columns, bins = 10, rem_ol = False, thres_1 = 0.05, thres_2 = 0.95):
    '''
    This function helps understand if polynomial terms and/or transformations are needed in a logistic regression. It calculates ln(p/(1-p)) of each bin of numerical columns.
    It also plot the ranges used, and a kernel distribution to help decide which transformation or polynomial term would help.
    If the relationship looks like linear, no need of polynomial term.
    Args:
        data: Input data-frame.
        outcome: Categorical variable that we will use to calculate ln(p/(1-p)).
        x_columns: Listing of column-names we wish to plot against outcome.
        bins: How many bins we will use to cut the numerical x column
        rem_ol: Remove anything lower than thres_1 percentile or higher than thres_2 percentile
        thres_1: Lower Percentile 
        thres_2: Higher Percentile 
    '''
    for x in x_columns:
        print('-'*100)
        print(f'{outcome} vs {x} -> rem_ol={rem_ol}')
        print('-'*100)

        # Reduce the number of columns
        data_clean = data[[outcome,x]]
        
        # If removal of outliers is preferred, the filter will remove all the observation lower than thres_1 percentile or higher than thres_2 percentile.
        if rem_ol:
            lim_1 = data_clean[x].quantile([thres_1]).iloc[0]
            lim_2 = data_clean[x].quantile([thres_2]).iloc[0]
            df = data_clean[(data_clean[x]>lim_1) & (data_clean[x]<lim_2)]   
        else:
            df = data_clean
        
        # Creates bins and calculates proportions of positive outcomes
        x_cat = pd.cut(df[x],bins=bins,retbins=True)
        p = df.groupby(x_cat[0])[outcome].sum()/df.groupby(x_cat[0])[outcome].count()
        
        # Integer indexes
        all_indexes = range(len(p))
        original_indexes = p.index
        p.index = all_indexes
        
        # Removes any bin with proportions of positive outcomes equals to 0 or 1 to avoid ln(0) or zero division. 
        p = pd.Series(p[(p.values>0) & (p.values<1)], index=p.index) 
        
        # ln(p/(1-p))
        log_odd = np.log(p/(1-p))

        # Relationships and kernel distribution graphs
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        g = log_odd.plot(marker='o', label='Values',ax=axes[0])
        missing_indexes = log_odd.index[log_odd.isna()]
        g.scatter(missing_indexes, log_odd[log_odd.isna()])
        g.set_xticks(all_indexes)
        sns.kdeplot(data=data_clean, x=x, ax=axes[1])
        axes[0].set_title(f'ln(p/(1-p)) of {outcome} vs {bins} {x} ranges')
        axes[1].set_title(f'{x} kernel distribution')
        plt.tight_layout()
        
        # Print the intervals used to create bins
        for i, int in enumerate(original_indexes):
            print(f'{i} = {original_indexes[i]}')

        # Plot 2 Graphs
        plt.show()

#%%
# Calling the function
ln_analysis(bat, 'hr_10', num_c )
