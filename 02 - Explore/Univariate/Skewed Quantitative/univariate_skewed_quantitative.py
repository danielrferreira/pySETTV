#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:03:50 2023

@author: danielferreira
"""

# Import Data
folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
import os
import pandas as pd
os.chdir(folder)
bat = pd.read_csv(file)
num_c = ['player_age', 'ab', 'pa', 'hit', 'single',
       'double', 'triple', 'home_run', 'strikeout', 'walk', 'k_percent',
       'bb_percent', 'batting_avg', 'slg_percent', 'on_base_percent',
       'on_base_plus_slg', 'b_rbi', 'r_total_caught_stealing',
       'r_total_stolen_base', 'exit_velocity_avg', 'sweet_spot_percent',
       'barrel_batted_rate', 'hp_to_1b', 'sprint_speed']

#%%
# We can use skew method to understand what are the most skewed columns:
bat[num_c].skew().sort_values()

#%%
# This function contains an argument to remove values greater than specific percentile: 
import seaborn as sns
import matplotlib.pyplot as plt
def hist_plots(data, columns, rem_ol=False, thres=0.99, scale_graph=9, n_cols=3, aspect_ratio=2/3 ):
    '''Create multiple Histograms plots using a subset of variables specified.
    
    Args:
        data: Input data-frame containing variables we wish to plot.
        columns: Listing of column-names we wish to plot.
        rem_ol: Remove observations greater than specific percentile defined by thres argument.
        thres: Percentile that will be used if rem_ol=True.
        scale_graph: Adjust the total size of the graph.
        n_cols: Adjust how many graphs we have on each row.
        aspect_ratio: Adjust the aspect ratio of each individual graph. For squared graphs use 1/1.
    '''

    # Adjusting how many rows the grid will have and proper sizes
    n_rows = len(columns)//n_cols+(len(columns)%n_cols>0) 
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(scale_graph, (scale_graph/n_cols)*aspect_ratio*n_rows))

    # Plotting
    fig.suptitle(f'Histograms of {len(columns)} columns',y=1, size=15)
    axes=axes.flatten()
    for i,feature in enumerate(columns):
        if rem_ol:
            lim = data[feature].quantile([thres]).iloc[0]
            x = data[feature][data[feature]<lim]
            print(f'{feature}: Observations greater than P{round(thres*100)} removed')
        else:
            x=data[feature]
        sns.histplot(data=x,ax=axes[i], kde=True)
    plt.tight_layout()

#%%
# Calling the function for skewed columns:
skewed = ['triple','r_total_caught_stealing','r_total_stolen_base']
hist_plots(data=bat,columns=skewed,rem_ol=True)

#%%
# Another option would be to see how they look like after a log transformation.
import numpy as np
ln_bat = np.log(bat[skewed]+1)
hist_plots(data=ln_bat,columns=skewed)
