#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:01:53 2023

@author: danielferreira
"""
#%%
# Cluster Analysis
#%%

#%%
# Imports and table
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
import os
folder = '/Users/danielferreira/Documents/repositories/pySETTV/06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
os.chdir(folder)
bat = pd.read_csv(file)
bat_23 = bat[bat['year']==2023]
num_c = ['player_age', 'ab', 'pa', 'hit', 'single',
       'double', 'triple', 'home_run', 'strikeout', 'walk', 'k_percent',
       'bb_percent', 'batting_avg', 'slg_percent', 'on_base_percent',
       'on_base_plus_slg', 'b_rbi', 'r_total_caught_stealing',
       'r_total_stolen_base', 'exit_velocity_avg', 'sweet_spot_percent',
       'barrel_batted_rate', 'hp_to_1b', 'sprint_speed', 'batting_avg']

subset = ['player_age', 'ab', 'on_base_plus_slg', 'exit_velocity_avg', 'sprint_speed']
bat_23_sub = bat_23[subset]
bat_23_sub = bat_23_sub[bat_23_sub['sprint_speed'].isna()==False]

#%%
# Exploration of inputs
#%%

#%%
# Correlations
print('Pearson Correlation')
plt.figure(figsize=(8,4))
sns.heatmap(bat_23_sub.corr(),annot=True, cmap='coolwarm')
plt.show()
print('Spearman Correlation')
plt.figure(figsize=(8,4))
sns.heatmap(bat_23_sub.corr(method='spearman'),annot=True, cmap='coolwarm')
plt.show()

#%%
# Standardization
#%%

#%%
# Because the euclidian distances can be more influenced by variables with higher scale, we need to rescale the data. Some people like to rescale the data using sklearn methods, like MinMaxScaler or StandardScaler:
scaler = StandardScaler()
data_standardized = scaler.fit_transform(bat_23_sub)

#%%
# You can also create a function yourself:
def min_max_scaler(x):
    return (x-x.min())/(x.max()-x.min())
scaled = bat_23_sub.copy()
for x in subset:
    scaled[x]= min_max_scaler(scaled[x])

#%%
# Optimal k
#%%

#%%
# In the past, we used hierarchical clustering with samples to define the best number of groups. If your data is not huge, you can run k-means multiple times to decide best k:
# Important to add limitations to n_init and max_iter according to your table size.
wcss = []  # Within-cluster sum of squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', n_init=100) #n_init is the number of different initial seeds, reduce if your data is large.
    kmeans.fit(scaled)
    wcss.append(kmeans.inertia_)
# Plot the elbow method
plt.plot(range(1, 11), wcss)
plt.title('Within-cluster sum of squares by k')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')  # Within-cluster sum of squares
plt.show()

#%%
# PCA can also helps
pca = PCA()
data_pca = pca.fit_transform(scaled)
plt.scatter(data_pca[:, 0], data_pca[:, 1])
plt.title('2D PCA Projection')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_explained_variance = np.cumsum(explained_variance_ratio)
plt.figure(figsize=(10, 6))
plt.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, align='center',label='Individual explained variance')
plt.step(range(1, len(explained_variance_ratio) + 1), cumulative_explained_variance, where='mid',label='Cumulative explained variance')
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance Ratio by Principal Components')
plt.legend()
plt.show()

#%%
# Final k-means
#%%

#%%
# Now that we dicided k, it is time run the final k-means algorithm. We usually increase max_iter and n_init.
kmeans_final = KMeans(n_clusters=3, init='k-means++', n_init=200, max_iter = 1000)
kmeans_final.fit(scaled)

#%%
# 2-D plot using PCA
scaled['Cluster'] = kmeans_final.labels_
plt.scatter(data_pca[:, 0], data_pca[:, 1],c=scaled['Cluster'], cmap='viridis')
plt.title('Clusters by 2D PCs')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

#%%
# Understanding results
#%%

#%%
# First step is to create the cluster column in the original dataset (before standardization)
bat_23_sub['Cluster'] = kmeans_final.labels_
# Be carefull with indexing here, I know the order was not changed, but it might be safer to use merge with proper indexes.

#%%
# Pie chart of frequency of each cluster
cluster_frequency = scaled['Cluster'].value_counts()
labels = cluster_frequency.index
sizes = cluster_frequency.values
plt.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%'.format(p))
plt.title('Cluster Frequency')
plt.show()

#%%
# Violin plots can be an interesting choice for cases where we have few final clusters.
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

violin_plots(bat_23_sub, 'Cluster', subset , n_cols = 2)
