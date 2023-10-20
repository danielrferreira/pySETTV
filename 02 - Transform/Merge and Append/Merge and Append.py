#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:19:42 2023

@author: danielferreira
"""

# You can ignore the code below, it just creates tables to use in the example:
from os import chdir
chdir('/Users/danielferreira/Documents/repositories/pySTETV/01 - Sample/Stratified')
import pandas as pd
baseball = pd.read_csv('batting_2021_2022_2023.csv', index_col='player_id')
bb_2022 = baseball[baseball['year']==2022]
bb_2023 = baseball[baseball['year']==2023]

#%%
# concat method can be used to stack tables
bb_2022_2023 = pd.concat([bb_2022,bb_2023])
print(len(bb_2022))
print(len(bb_2023))
print(len(bb_2022_2023))

#%%
# Joining tables if the have a proper index is easier as it can get:
# Preparing tables:
bb_2022['avg_2022']=bb_2022['batting_avg']   
bb_2022 = bb_2022[['name','avg_2022']]
bb_2023['avg_2023']=bb_2023['batting_avg']   
bb_2023 = bb_2023[['name','avg_2023']]
# Join:
all_years = bb_2022.merge(bb_2023, left_index=True, right_index=True, how='outer')
# Because name is in both tables we can combine then into a single column:
all_years['name'] = all_years['name_x'].combine_first(all_years['name_y'])
all_years = all_years[['name','avg_2022', 'avg_2023']]
# If the key for the join is not an index, you can use argument on (instead of left_index/right_index):
all_years = bb_2022.merge(bb_2023, on='name',how='outer')
    

#%%
# You can also change the how argument to reflect how you want your join (left and inner for instance)
all_years_left = bb_2022.merge(bb_2023, left_index=True, right_index=True, how='left')
all_years_inner = bb_2022.merge(bb_2023, left_index=True, right_index=True, how='inner')

#%%
# If you need to append or join multiple tables you can modify the code like this:
bb_2021 = baseball[baseball['year']==2021]
bb_2022 = baseball[baseball['year']==2022]
bb_2023 = baseball[baseball['year']==2023]
# Append
bb_2021_2022_2023 = pd.concat([bb_2021,bb_2022,bb_2023])
# Join
all_years = bb_2021.merge(bb_2022, left_index=True, right_index=True, how='outer').merge(bb_2023, left_index=True, right_index=True, how='outer')
