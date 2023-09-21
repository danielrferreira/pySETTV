#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 14:22:28 2023

@author: danielferreira
"""

# This code will have examples using VERY basic OOP concepts

#%%
# Object-Oriented Programming allow us to write less and "Don't Repeat Yourself" (DRY)
# Classes are a way to take advantage of inheritance 
# They have attributes and methods
# Creating an object from a class is known as instantiation
# self keyword refers to current object and helps access class variables
# def __init__(self,...) gets invoked automatically when the class is used

#%%
# Creating parent class
class author:
    # class variables (public scope)
    type_of_creator='Author'
    # class attributes
    def __init__(self,name,year_of_debut,country,type_author):
        self.name=name
        self.year_of_debut=year_of_debut
        self.country=country
        self.type_author=type_author
    # class method
    def print_name(self):
        print(self.name)
#%%
# Creating instances of the class
author_list=['']*3
author_list[0]=author('David Bowie',1966,'UK','Artist')
author_list[1]=author('The Beatles',1960,'UK','Band')
author_list[2]=author('The Beach Boys',1961,'US','Band')

#%%
# Accessing a method of the class
for i in [0,1,2]:
    author_list[i].print_name()

#%%
# Accessing an attribute of the class
for i in [0,1,2]:
    print(author_list[i].year_of_debut)

#%%
# Creating child (derived) class
class music_album(author):
    n_main_artist,type_of_content = 1,'Music' 
    def __init__(self,name,size,year,label):
        self.name=name
        self.size=size
        self.year=year
        self.label=label
    
#%%
# Creating an instance of the child class
first_album = music_album('Pet Sounds','Full',1966,'Capitol')

#%% Using parent and child variables
print('The type of creator is:',first_album.type_of_creator, '. And the name of album is:', first_album.name)

#%%
# Accessing a parent class variable on the child class
print(first_album.type_of_creator)

#%%
# Acessing a child class variable
print(first_album.type_of_content)

#%%
# Accessing a parent class method
first_album.print_name()

#%%
#Inheritance:
# 1) Single-level: Base Class -> Derived Class
# 2) Multi-level: Base Class -> Derived Class 1 -> Derived Class 2
# 3) Multiple: Base Class 1, Base Class2 -> Derived Class
# 4) Hierarchical: Base Class -> Derived Class 1, Derived Class 2
