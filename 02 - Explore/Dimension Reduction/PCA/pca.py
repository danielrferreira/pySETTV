#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:52:14 2023

@author: danielferreira
"""

from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
os.chdir(folder)
bat = pd.read_csv(file)
num_c = ['player_age', 'home_run', 'batting_avg','sweet_spot_percent','sprint_speed']
bat_pca = bat[num_c]
bat_pca = bat_pca[bat_pca['sprint_speed'].isna()==False]

#%%
# Running PCA is as easy as running any sklearn method
pca = PCA()
data_pca = pca.fit_transform(bat_pca)

#%%
# You can check the variance captured:
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_explained_variance = np.cumsum(explained_variance_ratio)
plt.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, align='center',label='Individual explained variance')
plt.step(range(1, len(explained_variance_ratio) + 1), cumulative_explained_variance, where='mid',label='Cumulative explained variance')
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance Ratio by Principal Components')
plt.legend()
plt.show()

#%%
# You can also check the cumulative variance captured printing the values:
for i, cumvar in enumerate(cumulative_explained_variance):
    print(f'PC{i+1} cumulative variance captured = {round(cumvar,3)}')

#%%
# Plotting the 2 first components is one way to visualizing the multidimensional data
plt.scatter(data_pca[:, 0], data_pca[:, 1])
plt.title('2D PCA Projection')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

#%%
# If you want a 3D version with 3 first components:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data_pca[:, 0], data_pca[:, 1], data_pca[:, 2])
ax.set_title('3D PCA Projection')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
plt.show()

#%%
# Lastly, you can use a loop and change the angles to better understand the 3D visualization:
angles = [[90,270,0],[0,270,0],[0,0,0],[45,45,45]]
for i,angle in enumerate(angles):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data_pca[:, 0], data_pca[:, 1], data_pca[:, 2])
    ax.view_init(elev=angle[0], azim=angle[1], roll=angle[2])
    ax.set_title(f'3D PCA Projection - View {i+1}')
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_zlabel('PC3')
    plt.show()
