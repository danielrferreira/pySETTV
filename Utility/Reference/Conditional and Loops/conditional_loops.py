#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:27:18 2023

@author: danielferreira
"""


#IF Statement
#%%
x = int(input('Enter a number: ')) 

if x>4:
    print('x > 4')

print('End')

#%%

#IF-ELSE Statement
#%%
x = int(input('Enter a number: ')) 

if x>4:
    print('x > 4')
else:
    print('x < 4')

#%%

#IF-ELSE Statement
#%%
x = int(input('Enter a number: ')) 

if x>4:
    print('x > 4')
else:
    print('x < 4')

#%%

#Nested IFs
#%%

x = int(input('Enter a number: ')) 

if x>=4:
    print('x > 4')
    if x>8:
        print('x > 8')
    else:
        print('4 < x < 8')   
else:
    print('x < 4')


#%%

#Short handed IFs 
#%%

x = int(input('Enter a number: '))

if x>4 : print('x > 4')

print('x > 5') if x>=5 else print('x < 5')

#%%

# While Loops
#%%

x = 1
while (x<10):
    x+=1
    print(x)

#%%

# Short handed IFs needs semicolon if in the same line
#%%

x = 1
while (x<10): x+=1; print(x)

#%%

# FOR Loops - iterate over sequence type objects
#%%

# Transversing over a string
for c in 'First Last':
    print(c)
#%%

#%%

# Transversing a List
letters = ['A', 'B', 'C', 'D']

for c in letters:
    print(c)

#%%


#%%

# Nested For
#%%

for i in [1,2,3,4]:
    for j in [2,3,4,5]:
        print(i*j)

#%%

# Nested For-While
#%%

i = 0

while (i*j<100):
    for j in [2,3,4,5]:
        print(i*j)
    print('')
    i+=1

#%%

#Break - Stop the loop
#%%
letters = ['A', 'B', 'C', 'D']

for c in letters:
    if c=='C':
            break
    print(c)
#%%

#Continue - Gets the loop to the next iteration
#%%
letters = ['A', 'B', 'C', 'D']

for c in letters:
    if c=='C':
        continue
    print(c)
#%%

#Pass - Null Statement, nothing happen. It has it applications when we don't 
# want to do anything with the if rule, but the else actions are important,
# see the second example
#%%
letters = ['A', 'B', 'C', 'D']

for c in letters:
    if c=='C':
        pass
    print(c)

print('')

for c in letters:
    if c=='C':
        pass
    else:
        print(c)

#%%
