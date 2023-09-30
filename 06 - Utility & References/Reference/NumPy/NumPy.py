#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:30:46 2023

@author: danielferreira
"""

# NumPy history goes back to 1995, when Jim Gugumin cretaed the numeric library. Until 2005, the array programming in python got fragmented. Travis Oliphant forged NumPy, bringing the community together around a single framework.

# It adds efficient methods to do mathematical operations including linear algebra, random number generation and Fourier transformation. It also added a C API to connect NumPy with C, C++ and FORTRAN libraries.

# Ndarray is an efficient multidimensional array that can be used to do matrix operations. NumPy-based algorithms are usually 10-100 more times faster than their pure Python counterparts.
import numpy as np

#%%
# NumPy Arrays
# An easy way to do mathematical operations. All elements must be the same data type.
a = np.array([1,2,3,4,5,6,7])
b = a*2
print(b)

#%%
# Important attributes and methods
x = np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(x)
print(x.shape,x.ndim,x.dtype)
y = np.zeros_like(x)
print(y)
z = np.ones_like(x)
print(z)
w = np.arange(10)
print(w)
a = np.identity(5)
print(a)

#%%
# When creating an array, you can also define the data type with the dtype argument:
a = np.array([1,2,3,4,5,6],dtype=np.float64)
print(a.dtype)
a = np.array([1,2,3,4,5,6],dtype=np.int32)
print(a.dtype)
colors = np.array(['Y','B','R','G','O','W'],dtype=np.string_)
print(colors.dtype)

#%%
# Basic Slicing (just like lists)
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a[0]
c = a[0,2]
d = a[0:2,1:3] # 0 and 1, 1 and 2
e = a[:,1]
to_be_printed = [a,b,c,d,e]
for i in to_be_printed:
    print(i)

#%%
# An important difference of numpy arrays is that all objects created from an array act as views, so updating the views will also update the original array:
print(e)
e[:]= 1
print(e)
print(a)
# If you need a copy, instead of a view, you shoud use copy() method.
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
e = a.copy()[:,1]
print(e)
e[:]= 1
print(e)
print(a)

#%%
# To filter arrays and datat frames in pandas, boolean indexing is one of the most usefull methods, imagine the following 4 arrays:
album = np.array(['The Clash','Give Em Enough Rope', 'London Calling', 'Sandinista!', 'Combat Rock','Cut The Crap'])
year = np.array([1977,1978,1979,1980,1982,1985])
charts_country = np.array(['UK', 'AUS', 'AUT', 'CAN', 'NOR', 'NZ', 'SPA', 'SWE', 'SWI', 'US'])
charts_pos = np.array([[12,None,None,None,None,None,None,42,None,126],[2,79,None,None,None,15,None,36,None,128],[9,16,17,12,4,12,52,2,72,27],[19,36,None,3,8,3,None,9,None,24],
[2,32,None,12,7,5,None,9,56,7],[16,69,None,59,None,35,None,30,None,88]])

print(album.shape)
print(year.shape)
print(charts_country.shape)
print(charts_pos.shape)   

# Arrays comparison would return an array of boolean values:
print(year<=1980)
# We can use this array to index the elements we need in any other array with same size and order:
print(f'Best Albums of Clash = {album[year<=1980]}')
# We can also work with multiple dimensions:
print(charts_pos[year<=1980,charts_country=='UK'])
# We can use ~ to invert the logic of a condition:
cond = album=='Cut The Crap'
great_albums = album[~cond]
print(great_albums)

#%%
# Transpose: Arrays have a T method that you can use to Transpose an array:
A = np.arange(21).reshape(3,7)
print(A)
B = A.T
print(B)
# You can also use swapaxes to do it. But this method will return a view of the array (without making a copy).
C = A.swapaxes(0,1)
print(C)
C[1] = 1
print(A)

#%%
# np.random module
# Numpy provided a faster than usual pseudorandom number generator. Usually, np.random methods are 2x faster than pandas sample, or built-in random module. Let's time the performance of np.random.standard_normal vs random.normalvariate(0,1)   
from random import normalvariate
import numpy as np
n=1000000
# Builtin Python module would take 278ms (in  average in my computer):
sample1 = [normalvariate(0,1) for _ in range(n)]
#  np.random would take 12.7ms (in  average in my computer)
sample2 = np.random.standard_normal(n) 
# The seed can be setted as a rng
high = np.random.default_rng(seed=410)
sample2 = high.standard_normal(n)
print(sample2[0])
# You can find more in the 01-Sample folder for applications and performance comparisons

#%%
# Fast operation-wise methods
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f'sqrt={np.sqrt(A)}\n')
print(f'exp={np.exp(A)}\n')

B = np.array([[4.1,5,6.75],[7.33,8.1,9],[1.2,2.3,3.1]])
remainder, whole_part = np.modf(B)
print(f'remainder={remainder}\n')
print(f'whole_part={whole_part}\n')

C = np.array([[4,5,6],[7,8,9],[1,2,3]])
print(f'add={np.add(A,C)}\n')
print(f'maximum={np.maximum(A,C)}\n')
print(f'minimum={np.minimum(A,C)}\n')
    
#%%
# Array-Oriented Programming  
# Arrays can save you time and the need of loops (while or for). Let's calculate all the possible distances between 2 points in a 2-D Grid:
import numpy as np
range_data = np.arange(-5,5,0.01) #1000 elements
x,y = np.meshgrid(range_data,range_data) #All possible combinations of range and range in two arrays. 
# x and y have 1000 elements each. x has the range in the first dimension, y has range in the second dimension   

# If we need to calculate the distance of each possible combinations, we could use two nested loops:
import math
dist1 = np.zeros_like(x)
for i in range(1000):
    for j in range(1000):
        dist1[i,j]  = math.sqrt(x[i,j]**2+y[i,j]**2)

# Instead, we can use array-oriented programming using a simple np.sqrt to do element-wise calculation:
dist2 = np.sqrt(x**2+y**2)

#%% 
# Where (Logics and Filters)
x = np.random.standard_normal(size=100)
y = np.where(x<0,-1,1) # Changes all negative values to -1 and all positives to 1.
print(y[:10])

#%%
# Statistical Methods
# There are many methods that summarize an array:
x = np.array([[1,2,3,11,5,6],[7,8,9,10,12,4]])
print(np.mean(x))
print(np.argmin(x))
print(np.argmax(x))
print(np.sum(x))
print(np.cumsum(x))

#%%
# Boolean are interpred as 1's and 0's if we use them in the previous statistical methods:
x = np.random.standard_normal(size = 100)
print((x>0)[0:10])
print(np.sum(x>0)) # count trues
print(np.mean(x>0)) # percent of trues

#%%
# sort() method can be used to sort the whole 1d array, or sort accross rows or columns.
x = np.random.standard_normal(size = 10)
y = np.sort(x)
print(y)
x = np.random.standard_normal((4,4))
print(x)
y = np.sort(x, axis=0) # Sorts whitin each columns
print(y)
y = np.sort(x, axis=1) # Sorts whitin each row
print(y)

#%%
# As an alternative to use sets (built-in python class), we can use np.unique to return an array with unique and sorted values.
x = np.array(['Joe', 'Bill', 'Bill', 'Will', 'Joe'])
y = np.unique(x)
print(y)  
    
# Another numpy alternative is to use these methods:
# in1d(): See if a value (or an array of values) is in another array
# setdiff1d(): Returns the difference between two values/arrays
# intersect1d(): Returns the intersection between two values/arrays
# union1d(): Returns the union between two values/arrays
# setxor1d(): Returns the symmetric difference (elements that are in either, but not both.

print(np.in1d(y,x)) # Is y in x?
y = np.array(['Bill','Suzy','Will'])
print(np.setdiff1d(y,x)) # What is in y that is not in x?  
       
#%%
# People usually prefers pandas to load and save data to files, numpy provides an option to save/load arrays.
x = np.array([1,2,6,8,9,10])
np.save("x_on_file", x)
y = np.load("x_on_file.npy")
print(y)    
# We can also save multiple arrays into a dictionary-like file using np.savez, or savez_compressed:
z = np.array(['Bob', 'Marley'])
np.savez("x_and_z_on_file", a = x, b = z)
# To load and use, you need to reference like a dictionary:
all = np.load("x_and_z_on_file.npz")
print(all['a'])
print(all['b'])

# There are many other methods and classes to learn about. One of the main usages of numpy is Algebra Linear
# You can find more about here:https://github.com/danielrferreira/py_play/tree/main/Linear%20Algebra
# Thanks to the numpy team we also have an amazing documentation here: https://numpy.org/
