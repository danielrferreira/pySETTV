#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:53:16 2023

@author: danielferreira
"""

# pandas is a module designed to work with tabular data structures. It contains common data manipulation methods and adopts significant parts of NumPy's idiomatic style of array-based programming (that will save you some "for loops"). It realies in two key data structures (classes):
# - Series
# - DataFrame

import pandas as pd
import numpy as np

###### SERIES ###########

#%%
# Series are objects with values and indexes. They are useful for moments that you might also use dictionaries.
y = pd.Series([10,20,30,60])
print(y)
# By default, Series constructor method creates sequential indexes, starting at zero. But you can change using the index keyword:
y = pd.Series([10,20,30,60],index=['a','b','c','d'])  
print(y)

#%%
# This index plays a key role on pandas, you can refer to a Series value using the index:
y['c'] = 90
print(y['b'])
print(y)

#%%
# array and index attributes will return the value and "labels"for the Series:
print(y.array)
print(y.index)

#%%
# Filtering the values will keep the index as it should:
print(y[y>50])
print(y*2)

#%%
# If you create a series using another with indexes that are not in the original one, pandas will treat them as missing (NaN)
y = pd.Series([10,20,30,60],index=['a','b','c','d'])
z = pd.Series(y,index=['b','c','e','d'])
z

#%%
# isna and notna have plenty of usages:
pd.isna(z)

#%%
# Simple missing imputation
y = pd.Series([10,20,30,60],index=['a','b','c','d'])
z = pd.Series(y,index=['b','c','e','d','f'])
z[pd.isna(z)] = np.mean(z)
z

#%%
# Another useful feature of pandas Series is that index are used to 'allign' data before any operation:
x = pd.Series([10,20],index=[1,2])
y = pd.Series([10,20],index=[2,1])
x+y

#%%
# Both the Series and the Series Index have name attributes:
x = [2001,2002,2003,2004,2005]
y = [12,20,22,38,45]
z = pd.Series(y,index=x)
print(z)
z.name = 'population'
z.index.name = 'year'
print(z)

#%%
###### DATA FRAMES ###########

#%%
# To represent tabular data (rectangular tables to be more precise), DataFrame objects are the most used class nowadays. It has both row and column indexes.    
album = ['The Clash','Give Em Enough Rope', 'London Calling', 'Sandinista!', 'Combat Rock','Cut The Crap']
year = [1977,1978,1979,1980,1982,1985]
UK_pos = [12, 2, 9, 19, 2, 16]
clash_dict = {'album_name':album,'year':year,'pos':UK_pos}
clash_pd = pd.DataFrame(clash_dict)
print(clash_pd)
clash_pd

#%%
# Useful methods
print(clash_pd.head()) # First 5 rows
print(clash_pd.tail()) # Last 5 rows

#%%
# keyword columns, can be used to define the order of the columns. If you include a columns that doesn't exists, a new column will be created:
clash_pd = pd.DataFrame(clash_dict, columns=['year','album_name', 'pos', 'original_label'])
clash_pd

#%%
# Columns can be accessed both using it's name or as an attribute of the DataFrame:
print(clash_pd['year'])
(clash_pd.year)

#%%
# You can also create new columns using the first method listed above:
clash_pd['age']=2023-clash_pd['year']
clash_pd

#%%
# To delete a column, you can use the del keyword:
del clash_pd['original_label']
clash_pd

#%%
# Just like numpy, you can use method T to transpose the data. Just remember that transposing will change data types sometimes:
clash_pd_t = clash_pd.T
print(clash_pd.dtypes)
print(clash_pd_t.dtypes)
clash_pd_t

#%%
# DataFrame Constructor
# pd.DataFrame can be used to create a new DataFrame object. Some of the possibles inputs for the method:
# 2D ndarray, Dictionaries of series, arrays, lists or tuples (just like the examples I already used)
# List of Lists, Another DataFrame

#%%
# Understanding indexes as objects are key to understand how to handle and transform DataFrames, any DataFrame have indexes as objects:
album = ['The Clash','Give Em Enough Rope', 'London Calling', 'Sandinista!', 'Combat Rock','Cut The Crap']
year = [1977,1978,1979,1980,1982,1985]
UK_pos = [12, 2, 9, 19, 2, 16]
clash_dict = {'year':year,'pos':UK_pos}
clash_pd = pd.DataFrame(clash_dict,index=album)
clash_pd.index

#%% 
# As an index object, they are immutable and can be used in 'in' operations:
print(clash_pd.index[0])
clash_pd.index[0] = 'The Clash (UK)'  # Not going to work

#%%
print('The Clash (UK)' in clash_pd.index)

#%%
# Reindexing
album = ['The Clash','Give Em Enough Rope', 'London Calling', 'Sandinista!', 'Combat Rock','Cut The Crap']
year = [1977,1978,1979,1980,1982,1985]
UK_pos = [12, 2, 9, 19, 2, 16]
clash_dict = {'album_name':album,'pos':UK_pos}
clash_pd = pd.DataFrame(clash_dict,index=year)
clash_pd.index.name = 'year'
clash_pd
clash_2 = clash_pd.reindex(range(1977,1986,1),method='ffill') #method='ffill' fills the blanks with previous values
clash_2

#%%
# You can drop rows and columns using indexes with drop method:
clash_3 = clash_2.drop(1980)
clash_3
clash_4 = clash_3.drop('pos',axis=1)
clash_4

#%%
# Slicing with loc and iloc methods
# Using integer positions to slice data (just like in numpy arrays and lists) can return unexpected results, since some dataframes can have integer as labels. Using loc (based on labels) and iloc (based on integer position) can help differentiate for different cases.
clash_2.iloc[1:3]
clash_2.loc[1:3]
clash_2.loc[1978:1980] #Important to notice that ranges are inclusive on loc method
clash_2.loc[1978:1980, 'pos'] # Return a series

#%%
# Data Alignment
# When the data is indexed, the default is to use the index to allign the data before any calculus:
x1 = pd.DataFrame({'A1':[1,2,3,4,5],'B1':[6,7,8,9,10]}, index=[1,2,3,4,5])
x2 = pd.DataFrame({'A1':[1,2,3,4,5],'B1':[6,7,8,9,10]}, index=[3,2,1,5,4])
y = x1['A1']+x2['A1'] 
y

#%%
# For cases where you have missing and you want to fill missing before any calculus you can use fill_value in arithmetics methods
x1 = pd.DataFrame({'A1':[1,np.nan,3,4,5],'B1':[6,7,8,9,10]}, index=[1,2,3,4,5])
x2 = pd.DataFrame({'A1':[1,2,3,4,5],'B1':[6,7,8,9,10]}, index=[3,2,1,5,4])
y1 = x1['A1']+x2['A1'] 
y2 = x1['A1'].add(x2['A1'],fill_value=0)
print(y1) # Missing
print(y2) # No Missing

#%%
# Some of the possible arithmetic methods:
# add, radd, sub, rsub, div, rdiv, floordiv, rfloordiv, mul, rmul, pow, rpow
# r stands for reversed, so 1/df => df.rdiv(1)

#%%
# Broadcasting
# When doing operations across Sereies and DataFrames, by default, the index of the Series matches the columns of the Data Frame.
expectional_case = pd.Series([10,20,30],index=['x1','x2','x3'])
df = pd.DataFrame({'x1':[1,2,3,4,5],'x2':[2,4,6,8,10],'x3':[3,6,9,12,15]})
df+expectional_case

#%%
# If DataFrame or Series have different indexes, the result will be the union:
expectional_case = pd.Series([10,20,30,40],index=['x1','x2','x3','x4'])
df = pd.DataFrame({'x1':[1,2,3,4,5],'x2':[2,4,6,8,10],'x3':[3,6,9,12,15],'x5':[5,10,15,20,25]})
df+expectional_case

#%%
# Because the calculus occur for each row, we say it is broadcasting over the rows, if you want to broadcast over columns you need to use an arithmetic method with argument axis='index'
new_feature = pd.Series([10,20,30,40,50])
df = pd.DataFrame({'x1':[1,2,3,4,5],'x2':[2,4,6,8,10],'x3':[3,6,9,12,15]})
df.add(new_feature) # Wrong, still broadcasting over columns
df.add(new_feature,axis='index') # Bam!!!

#%%
# Function Application using apply
# Apply is an usefull method for data manipulation, many times we need to do the same thing accross columns or rows. Creating a function (or a lambda function) and then refering it using apply can help.
# Let's say we need to normalize the data to squeeze all values to be between 0 and 1
from os import chdir
chdir('../../06 - Utility & References/Data')
import pandas as pd
baseball_raw = pd.read_csv('batting_2021_2022_2023.csv', index_col='player_id')
baseball = baseball_raw[['player_age', 'home_run', 'k_percent', 'bb_percent','batting_avg','sprint_speed']]
def min_max(x):
    return (x-x.min())/(x.max()-x.min())
baseball = baseball.apply(min_max)
baseball.head()

#%%
# By default, apply is invoked once per column, if you want to be invoked once for each row, you sould use axis='columns'
baseball = baseball_raw[['player_age', 'home_run', 'k_percent', 'bb_percent','batting_avg','sprint_speed']] #Just gathering the original values
baseball = baseball.apply(min_max, axis='columns') # Important: In a Data Analysis context, this doesn't make a lot of sense
baseball.head() 

#%%
# Sorting and Ranking
# Series
batting_avg = baseball_raw['batting_avg']
batting_avg.sort_index()
batting_avg.sort_values()

#%%
# DataFrames
baseball = baseball_raw[['name','player_age','batting_avg']]
baseball.sort_index()
baseball.sort_values('batting_avg')
baseball.sort_values('batting_avg', ascending=False)

#%%
# Rank works in the same way, but returns a rank (instead of the original value). It also keep the order of the values intact:
batting_avg.rank() # Series
baseball.rank() # For DataFrames, it broadcasts for each column

#%%
# Rank has tie-breaking methods:
# average, 
# min (Use the minimum rank for all tied values, next group will have rank=+number of elements in previous group)
# max (Use the maximum rank for all tied values)
# first (Assign rank in the order the values appear)
# dense (linke min, but next group will have +1 rank)
# Important: The table used in this example has duplicate indexes, be aware that this can return unwanted results. For instance, if there was only unique values, batting_avg[443558] would return a scalar, in this table the same code will return a Series.
batting_avg[443558]
batting_avg.index.is_unique

#%%
# Summarizing Data
# DataFrames and Series have many summarizing methods, such as sum() and mean()
baseball = baseball_raw[['player_age', 'home_run', 'k_percent', 'bb_percent','batting_avg','sprint_speed']]
baseball.mean() # Returns a Series with name of columns as indexes
# By default, the methods ignores missing, use skipna=False if you want it otherwise.

#%%
# Correlation and Covariance
baseball['player_age'].corr(baseball['batting_avg'])
baseball['player_age'].corr(baseball['sprint_speed'])
# For pair-wise (1xn) correlation, you can use corrwith:
baseball.corrwith(baseball['batting_avg'])   

#%%
# Spoiler: we can also use seaborn module to plot correlations heatmap
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
sns.heatmap(baseball.corr(numeric_only=True),annot=True, cmap='coolwarm')
plt.show()

#%%
# Value Counts
# For categorical features, we can use value_counts
baseball['player_age'].value_counts().sort_index()   
