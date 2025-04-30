#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:29:12 2023

@author: danielferreira
"""

#%%
# Modules are others .py source codes that we can incorporate in our code
# you can find the modules .py in the lib directory
# Example of path where the .py are/Users/<user_name>/Library/Python/3.9/lib/python

#%%
#import statement : is going to import all functionalities of a py
import math 
math.dist([0,0,0], [1,1,1]) #calculates the distance between 2 coordenates in a nd dimension
#math is already a standard module

#%%
# Creating modules: save a .py with functions, classes and variables in one of the following paths:
# 1) current working directory
# 2) PYTHONPATH
# 3) installation-dependent default path
# Then you need to import the file

#-----df_module.py-----#
# def soma(x,y):
#   return x+y

# def multiplication(x,y):
#   return x*y
# z=1
#---------------------#

import df_module as nm
print(nm.soma(2,3))
print(nm.multiplication(2,3))
print(nm.z)

#%%
# From-import can make even smoother to call it
from df_module import soma
print(soma(2,3))


#%%
# dir() can be used to see all functions,classes and variables 
import math
print(dir(math))
import os
print(dir(os))
import numpy
print(dir(numpy))

#%%
# Packages are an organized and well-structired hierarchies of folders
# A package have a __init__.py file with all the import statements ot the:
# 1)sub-packages
# 2)modules
# 3)sub_modules

#%%
# Package creation
# 1) Create a directory where Python is running
# 2) Place the modules and sub m-modules (.py)
# 3) create a __init__.py with all the import statements needed

#%%
# In this example I created a folder called df_pack, inside there is 3 .py files:
# df_module_1, df_module_2 and __init__.py
import df_pack
df_pack.df_module_1.soma(1,2)

#%%
# This example uses a function inside df_module_2 that import a txt into a dictionary
header = ('artist','album','country','region','year_artist','label','year_album')                   
input_file='06 - Utility & References/Data/input2.txt'
db = df_pack.df_module_2.import_file(input_file,header)  












