#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:21:26 2023

@author: danielferreira
"""
##########################################################################
#                                                                        #
# This code provides a function that imports the following data formats: #
#   1) csv                                                               #
#   2) excel                                                             #
#   3) sas                                                               #
#   4) spss                                                              #
#   5) stata                                                             #
#                                                                        #
# It requires only 1 parameters: file_in                                 #
# There is also 1 optional parameters: delimiter                         #
#                                                                        #
##########################################################################

#%%
def read_all(file_in,delimiter=','):
    # This function import 5 types of files
    from pandas import read_csv,read_excel,read_sas,read_spss,read_stata
    pos = len(file_in)
    while pos > -8:
        if file_in[pos-1]=='.':
            data_type=file_in[pos:len(file_in)]
            break
        pos -= 1
    try:
        if data_type=='csv':
            result = read_csv(file_in,sep=delimiter)
        elif data_type in ('xlsx','xls'):
            result = read_excel(file_in)
        elif data_type=='sas7bdat':
            result = read_sas(file_in)
        elif data_type=='sav':
            result = read_spss(file_in)
        elif data_type=='dta':
            result = read_stata(file_in)
    except:
        print('Something is off')
        success = False
    else:
        success = True
    if success:
        print('File with',data_type,'extension imported successfully')
        return result
    
#%%
# How to call the function:
titanic = read_all('/Users/jimihendrix/Documents/repositories/pySTETV/Utility/File Import/raw data/titanic.csv')
