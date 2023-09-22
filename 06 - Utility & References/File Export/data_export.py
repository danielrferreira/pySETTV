#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:30:51 2023

@author: danielferreira
"""

# Export DataFrames
# The easiest way to export a data set is using the to_csv method from pandas.

# You will only need pandas, os and numpy is only creating the data.
import numpy as np
import pandas as pd
height = np.round(np.random.normal(loc=170, scale=2, size = 100),2)
weight = np.round(height*0.4 +np.random.normal(loc=0, scale=7, size = 100),2)
height_and_weight = pd.DataFrame({'height':height,'weight':weight})

#%%
# Simple to_csv usage
height_and_weight.to_csv('output1.csv', index=False)

#%%
# Other usefull arguments
# index=True would add an index (0,1,2,3,...)
height_and_weight.to_csv('output2.csv', index=True)
# sep to change the delimiter
height_and_weight.to_csv('output3.csv', index=False, sep=';')

#%%
# mode='w' is the default, but you can change to 'a' if you want to add new rows to the existing file
new_rows = pd.DataFrame({'height':[168,180,150],'weight':[75.5,74,61]})
new_rows.to_csv('output1.csv', header=False,index=False, mode='a')

#%%
# Other formats:
height_and_weight.to_excel('output1.xlsx', sheet_name='Sheet1', index=False)
height_and_weight.to_json('output1.json', orient='records', lines=True)

#%%
# Alternatives to to_csv
# csv module
import csv
with open('output4.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(height_and_weight.columns)
    for row in height_and_weight.values:
        csvwriter.writerow(row)
#%%
# write method combined with pd.DataFrame.to_string (Careful, by default doesn't use , as separators)
with open('output5.csv', 'w') as f:
    f.write(height_and_weight.to_string(index=False))

#%%
# numpy savetxt
import numpy as np
np.savetxt('output6.csv', height_and_weight.values, delimiter=',', fmt='%s', header=','.join(height_and_weight.columns), comments='')