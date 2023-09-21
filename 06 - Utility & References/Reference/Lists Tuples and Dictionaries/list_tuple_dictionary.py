#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:46:48 2023

@author: danielferreira
"""

#Lists

#Lists characteristics
# Mutable, non-homogeneous (different data-types in one list), first index is 0

#%%
# Creating Lists and accessing elements
#%%
x = [1,2,'A',True, False, 3.14,-2]
print(x[0])
print(x[2])
print(x[4])
print(x[5])

#%%
# Negative Index
print(x[-6])
print(x[-4])
print(x[-2])
print(x[-1])

#%%
#Types of errors
print(x[7]) #Index Error
print(x[2.5]) #Type Error

#%%
#Slicing Lists - Start is inclusive, Stop is exclusive
print(x)
print(x[:])
print(x[3:])
print(x[0:3]) #0,1,2 elements
print(x[0:5:2]) #Skip 1 element by step
print(x[0:7:3]) #Skip 2 elements by step

#%%
#Changing List elements
x[1]='B'
print(x)
x[0:2]=2,3,'B'
print(x)

#%%
#Adding Elements to the List using Append(), Insert() and Extend()
#%%
#Append is used to add at the end of the list
x=[1,2,3]
print(x)
x.append(4)
print(x)
i=5
while (i<=30):
    x.append(i)
    i+=1
print(x)

#%%
#Insert can be used to choose the position of the new element, 
#it doesn't replace like a simple assigment statement, it pushes other elements
# to different positions. It requires 2 arguments.
x = ['A','B','C','D']
x.insert(2,'X')
print(x)

#%%
#Extend - Combines lists and adds multiple elements at the End
x = [1,2,3]
y = ['A',4]
x.extend(y)
print(x)
x.extend([5,6])
print(x)

#%%
#Removing elements with pop(), remove() and del
#%%
#pop() removes the last element, if you add an index argument, it removes the 
#element at that position
x = [1,2,3]
y = ['A',4]
x.extend(y)
print(x)
x.pop()
print(x)
x.pop(2)
print(x)

#%%
#remove() requires the value you want to remove, not the index.
#It removes one element at a time. You need a loop to remove multiple.
x = [1,'A',2,'A','B','A',True]
x.remove('A')
print(x)

x = [1,'A',2,'A','B','A',True]
while ('A' in x):
    x.remove('A')
print(x)

#Important: the argument is not an index, remove(1) will remove the 0th element
# (1) not the element at position=1 ('A')
x = [1,'A',2,'A','B','A',True]
x.remove(1)
print(x)

#%%
#del keyword is used to delete an element like pop did, but is not a function
x = ['A','B','C','D']
del x[2]
print(x)

#%%
#Other built-in functions
#%%
x = ['A','B','C','D']
len(x) #returns the length of the list (last index + 1 because the first is 0)
y = (12,23,34,45)
z = list(y) #convertsa a tuple into a list
max(z),min(z) #return maximun/minimum, it can be used with characters and numbers, but
#  only one type at a time, if you have a non homogeneus list, TypeError will 
# appear
#%%
x = ['A','B','C','D',12,23]
max(x) #TypeError
#%%
#Other functions and operators
x = [2,3,1,4,6,3]
print(x.count(3)) #returns 2 as there are 2 3's at the list
print(x.index(3)) # 1 since 3 is at the position 1 
x.reverse() #transform x
x.sort() #Sort x
y = x.copy()
z = ['A']*4 # Creates a list with 4 A's
w = ['A','B']+['A','B']+x #concatenates like extend()
x.clear() #Removes all the elements
print(3 in y)
print(3 not in y)

#%%
#Tuples
# Just like lists, but immutable. Usually performs better, can be used as keys
#%%
#Creation
tuple1 = (1,2,3,6)
#Reference
print(tuple1[1])
#Single element tupple should have commas in the assigments
x=('A',)
y=('A')
print(type(x)) #tuple
print(type(y)) #str

#You can use most of the functions and operators you used with lists, the
#exception are the ones that updates values
del x

#%%
#Can't be updated
tuple1[2]=3#TypeError

#%%
#Dictionaries, Creation and access, Keys imutable
import datetime as dt
bowie1 = {'first_name':'David', 'last_name':'Bowie', 'dob':dt.datetime(1947,1,8)}
bowie2 = dict([('first_name','David'),('last_name','Bowie'),('dob',dt.datetime(1947,1,8))])    
print(bowie1['last_name'])    
print(bowie2['dob'].strftime('%B %d, %Y'))    

#%%
x=bowie1['middle_name'] #KeyError   

#%%
#To change values
bowie1['last_name'] = 'Jones' #Updating a Value from an existing key
bowie1['middle_name'] = 'Robert' #New Key and Value 
print(bowie1)    
    
#%%
#Removing pairs of key:value
bowie = {'first_name':'David','middle_name':'Robert','last_name':'Bowie', 'dob':dt.datetime(1947,1,8)}
bowie.pop('middle_name')
print(bowie)        
bowie.popitem()          
print(bowie)

#%%
#Deleting and clearing dictionary
del bowie1
bowie2.clear()

#%%
#Dictionaries Handling Functions
bowie = {'first_name':'David','middle_name':'Robert','last_name':'Jones', 'dob':dt.datetime(1947,1,8)}
print('Length = ',len(bowie))
print('Keys = ',bowie.keys())
print('Values = ',bowie.values())
print('Keys:Values = ',bowie.items())

#%%
#Logical functions
x = {1:True, 2:False, 3:False}
#print(x.has_key('name')) #False - Discontinued in Python 3 - we can use 'in' operator
#print(x.has_key(2)) #True
print(all(x)) #True, because it look at key and not values, all keys are >0
print(any(x)) #True
x = {0:True, 2:False, 3:False}
print(all(x)) #False
