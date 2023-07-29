#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 22:28:29 2023

@author: danielferreira
"""

# Functions

#%%
#Built-In Functions

#%%
#There are multiple built-in functions, such as type, len and print
x=[1,2]
print(len(x))
print(type(x))

#%%
#User-defined functions

#%%
#Functions created by users, it can return a value or a none-type object

#%%
#def keyword to create function, we also need the name of the function, 
#parenthesis, : and an indented block of code 
#It is a good practice to add docstrin to document after the def keyword
import math as ma
def distance_from_origin(x,y):
    #This function uses basic trigonometric to calculate distance from (0,0)
    return ma.sqrt(x**2+y**2)
distance_from_origin(2, 2)

#%%
#Return is optional, 2 examples using the same function
def distance_from_origin1(x,y):
    #This function uses basic trigonometric to calculate distance from (0,0)
    return ma.sqrt(x**2+y**2)
print(distance_from_origin1(3, 2))

def distance_from_origin2(x,y):
    #This function uses basic trigonometric to calculate distance from (0,0)
    print(ma.sqrt(x**2+y**2))
distance_from_origin2(3,2)

#%%
#Three Types of Arguments
#Required, Default, Keyword, Variable Length

#%%
#Required is the one used, you declare the function by naming the arguments
#Order is respected.
def distance_from_origin1(x,y):
    #This function uses basic trigonometric to calculate distance from (0,0)
    return ma.sqrt(x**2+y**2)
print(distance_from_origin1(3, 2))

#%%
#Default is when you sets a default value for an argument
def distance_from_origin1(x,y=2):
    #This function uses basic trigonometric to calculate distance from (0,0)
    return ma.sqrt(x**2+y**2)
print(distance_from_origin1(3)) #Only x is provided

#%%
#Keyword uses the same syntax as required or default to declare, but you can 
#call the function using the name of the argument
def distance_from_origin1(x,y):
    #This function uses basic trigonometric to calculate distance from (0,0)
    return ma.sqrt(x**2+y**2)
print(distance_from_origin1(y=10, x=2))

#%%
# Variable length is useful when you don't know how many arguments you need
# the argument is passed as a tuple to the block of function code
def sum_all(*args):
    #This function adds all the values provided
    return sum(args)
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8,9,10))

#%%
#Global vs Local Variables

#%%
#Global variables are assigned out of functions and can be accessed anywhere
x=1
print(x) #used out of the function
def test():
    return 2+x #used inside function
print(test())

#%%
#Local variables are assigned inside function and are only available inside
#the function
def test():
    x=100
test()
print(x) #Will output 1 because of last example, or NameError if you don't
#ran the previous examples














