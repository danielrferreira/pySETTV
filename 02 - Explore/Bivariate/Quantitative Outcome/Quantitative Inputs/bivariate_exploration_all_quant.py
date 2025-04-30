#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:24:45 2023

@author: danielferreira
"""

# Import dataframe and modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
os.chdir(folder)
bat = pd.read_csv(file)
num_c = ['player_age', 'ab', 'pa', 'hit', 'single',
       'double', 'triple', 'home_run', 'strikeout', 'walk', 'k_percent',
       'bb_percent', 'slg_percent', 'on_base_percent',
       'on_base_plus_slg', 'b_rbi', 'r_total_caught_stealing',
       'r_total_stolen_base', 'exit_velocity_avg', 'sweet_spot_percent',
       'barrel_batted_rate', 'hp_to_1b', 'sprint_speed']
outcome = 'batting_avg'
x = 'player_age'
data = bat

#%%
# This code explore 3 options to understand relationships between quantitative columns:
# - Correlations 
# - Scatter Plots (If n too high, we will use samples)
# - Hexbin (hexagonals with colors representing frequencies)

#%%
# Simple Pearson Correlation
data[outcome].corr(data[x])

#%%
# Simple Spearman Correlation
data[outcome].corr(data[x],method='spearman')

#%%
# Simple Scatter Plot
plt.scatter(x=data[x],y=data[outcome])
plt.title(f'{x} vs {outcome}')
plt.show()

#%%
# Simple Hexbin Plot (Each hexagonal will be colored as the frequency)
plt.hexbin(x=bat[x], y=data[outcome], gridsize=25, cmap='Blues')
plt.title(f'{x} vs {outcome}')
plt.show()

#%%
# When we have a list with all numerical columns we want to correlate with the outcome, we can use corrwith
data[num_c].corrwith(data[outcome])

#%%
# If you want a visual display, you can use this function
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
corr_graph(bat,'batting_avg',num_c)

#%%
# Using Spearman
corr_graph(bat,'batting_avg',num_c, c_method='spearman')

#%%
# This next function create pair-wise scatter plots using samples:
def scatter_plots(data, outcome, x_columns, max_points = 1000, seed=420,  scale_graph=9, n_cols=3, aspect_ratio=2/3 ):
    '''Create pair-wise scatter plots (outcome vs x columns).
    
    Args:
        data: Input data-frame.
        outcome: Numerical variable we will plot in the y axis.
        x_columns: Listing of column-names we wish to plot against outcome.
        max_points: if len(data) > data_points, than a sample will be used.
        seed: Random seed used in the sampling.
        scale_graph: Adjust the total size of the graph.
        n_cols: Adjust how many graphs we have on each row.
        aspect_ratio: Adjust the aspect ratio of each individual graph. For squared graphs use 1/1.
    '''
    # Sample the data if needed. Scatter Plots can be expensive.
    if len(data) > max_points:
        indices = np.random.choice(data.index, size=max_points, replace=False)
        data_sample = data.loc[indices]
        n = max_points
        message = 'Sample Used'
    else:
        data_sample = data
        n = len(data)
        message = 'Full data used'
    
    # Adjusting how many rows the grid will have and proper sizes
    n_rows = len(x_columns)//n_cols+(len(x_columns)%n_cols>0) 
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(scale_graph, (scale_graph/n_cols)*aspect_ratio*n_rows))

    # Plotting
    fig.suptitle(f'Scatter plots of {len(x_columns)} columns by {outcome}. {message} (n={n}).',y=1, size=15)
    axes=axes.flatten()
    for i,feature in enumerate(x_columns):
        c = data[outcome].corr(data[feature])
        axes[i].set_title(f'{feature}: r = {round(c,2)}')
        axes[i].scatter(y=data_sample[outcome], x=data_sample[feature])
    plt.tight_layout()   

#%%
# Calling the function
scatter_plots(bat,outcome, num_c)

#%%
# Hexbin multiple graphs
def hexbin_plots(data, outcome, x_columns, gs = 25, scale_graph=9, n_cols=3, aspect_ratio=2/3 ):
    '''Create pair-wise hexbin plots (outcome vs x columns). BE CAREFUL: THIS FUNCTION IS COMPUTATIONAL EXPENSIVE WITH BIG TABLES.
    
    Args:
        data: Input data-frame.
        outcome: Numerical variable we will plot in the y axis.
        x_columns: Listing of column-names we wish to plot against outcome.
        gridsize: The size of each hexagonal bins.
        scale_graph: Adjust the total size of the graph.
        n_cols: Adjust how many graphs we have on each row.
        aspect_ratio: Adjust the aspect ratio of each individual graph. For squared graphs use 1/1.
    '''
    # Adjusting how many rows the grid will have and proper sizes
    n_rows = len(x_columns)//n_cols+(len(x_columns)%n_cols>0) 
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(scale_graph, (scale_graph/n_cols)*aspect_ratio*n_rows))

    # Plotting
    fig.suptitle(f'Hexbin plots of {len(x_columns)} columns by {outcome}.',y=1, size=15)
    axes=axes.flatten()
    for i,feature in enumerate(x_columns):
        c = data[outcome].corr(data[feature])
        axes[i].set_title(f'{feature}: r = {round(c,2)}')
        axes[i].hexbin(y=data[outcome], x=data[feature],gridsize=gs, cmap='Blues')
    plt.tight_layout()

#%%
# Calling the function
hexbin_plots(bat,outcome, num_c)

#%%
# Another tool to understand quantitative relationships is to create correlation heatmaps
all_num = num_c + [outcome]
plt.figure(figsize=(15,10))
sns.heatmap(bat[all_num].corr(), annot = True, cmap='coolwarm')
plt.show()
