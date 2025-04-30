#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 09:31:24 2023

@author: danielferreira
"""
# Example Data
import numpy as np
import pandas as pd
height = np.round(np.random.normal(loc=170, scale=2, size = 100),2)
weight = np.round(height*0.4 +np.random.normal(loc=0, scale=0.8, size = 100),2)
height_and_weight = pd.DataFrame({'height':height,'weight':weight})

#%%
# Remember to change your working directory. In Jupyter, you can use %cd command, or use os module:
from os import chdir
chdir('../../06 - Utility & References/Data/Export') 

#%% pyplot.savefig method is the only thing we will need:
import matplotlib.pyplot as plt
plt.scatter(height_and_weight['height'], height_and_weight['weight'])
plt.title('Height vs Weight Relationship')
plt.savefig('height_weight1.png')
plt.close() # Depending on your evironment, this won't be needed

#%%
# Use figure method to change the size of the file/graph:
plt.figure(figsize=(5, 2.5))
plt.scatter(height_and_weight['height'], height_and_weight['weight'])
plt.title('Height vs Weight Relationship Small')
plt.savefig('height_weight_small.png')
plt.close() # Depending on your evironment, this won't be needed

#%%
plt.figure(figsize=(20, 10))
plt.scatter(height_and_weight['height'], height_and_weight['weight'])
plt.title('Height vs Weight Relationship Big')
plt.savefig('height_weight_big.png')
plt.close() # Depending on your evironment, this won't be needed

#%%
plt.figure(figsize=(10, 10))
plt.scatter(height_and_weight['height'], height_and_weight['weight'])
plt.title('Height vs Weight Relationship Square')
plt.savefig('height_weight_square.png')
plt.close() # Depending on your evironment, this won't be needed

#%%
# You can also use savefig to save PDF's
plt.scatter(height_and_weight['height'], height_and_weight['weight'])
plt.title('Height vs Weight Relationship - PDF Version')
plt.savefig('height_weight1.pdf', format='pdf')
plt.clf()
