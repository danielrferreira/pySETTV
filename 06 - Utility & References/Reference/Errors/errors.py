#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 11:55:23 2023

@author: danielferreira
"""

# This code will provide types of errors, examples, and tools to handle logical errors

#%%
# Errors in Python can be classified into two types:
# 1) Syntax Errors: This are raised on compile, mostly due to typos and wrong indentation
# 2) Logical Errors: Raised on execution, can make your results be different than expected

#%%
# Errors with examples:
    
# AssertionError: Assert statement fails to execute
# AttributeError: An attribute of a class not found
# ModuleNotFoundError (Old ImportError): Import statement doesn't find a module or package
# IndexError: Index doesn't exists ina list or tuple
# KeyError: Key is not found in memory
# NameError: Identifier not found in global or local scope
# ValueError: Number exceeds the limit for the 
# SyntaxError: When the code doesn't follow the proper syntax
# IndentationError: Indentation mismatch
# TypeError: Operation not supported for that specific data type
# ZeroDivisionError: x/0

#%%
# Assertion Error (AssertionError)
x=0
assert x!=0

#%%
# Attribute Error (AttributeError)
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")
print(person.location)

#%%
# Module Not Found Error (ModuleNotFoundError)
import beatles

#%%
# Index Error (IndexError)
x = [2,3,4]
y = x[3]

#%%
# Key Error (KeyError)
x={0:1,1:2}
x['a']

#%%
# Name Error (NameError)
z=variable_that_doesnt_exist

#%%
# Syntax Error(SyntaxError)
x=sum(1,2

#%%      
# Indentation Error (IndentationError)
for i in [0,1]:
print(i)

#%%
# Type Error (TypeError)
x='3'
y=2
z=x/y

#%% 
# zero Division (ZeroDivisionError)
x=3/0

#%%
# Other types of errors

# EOFError: When end of file is reached while an input() is performing
# GeneratorExit: close() is invoked
# FloatingPointError: Floating point operation fails
# KeyboardInterupt: Ctrl+C during execution
# MemoryError: Memory limit reached
# NotImplementedError: Abstract function doen't get implemented
# OSError: Operational System related error (Windows, Unix, ...)
# OverflowError: Number exceeds the limit for the specific data type
# RuntimeError: Error does not fall in any other exception categories
# StopIteration: next() doesn't find any object to point in a generator object
# TabError: Tab or space mismatch
# SystemError: Interpreter internal error but the interpreter doesn't get an exit
# SystemExit: auto sys.exit() function was called
# UnboundLocalError: Local variable not assigned with a value 
# UnicodeError: Unicode-related encoding or decoding error inside a program 
# ValueError: Values suplied not appropriate



#%%
# Handling Exceptions with try, except, else and finally statements

#%%
x = 3
y = 0
z=x/y
print(z) #ZeroDivisionError if y is 0

#%%
# This code would return a ZeroDivisionError. What we can do is use 
# try/exception/finally statements to overcome the error
# try test if works, if it works it runs, if not it checks for the exception 
# listed in the except statement. finnaly will always run

#%%
# Solution:
x = 3
y = 0
try:
    z=x/y
except ZeroDivisionError:
    z=9999
    print('Zero Division was avoided, 9999 was passed instead')
finally:    
    print(z)

#%% 
# else can also be used to run something if no exception is found
x = 3
y = 0
try:
    z=x/y
except ZeroDivisionError:
    z=9999
    print('Zero Division was avoided, 9999 was passed instead')
else:
    print('No Zero Division Found')
finally:    
    print(z)

#%%
# This code would have the same result, but only because the print is placed
# after the ZeroDivisionError (the code block stop before the print)
x = 3
y = 0
try:
    z=x/y
    print('No Zero Division Found')
except ZeroDivisionError:
    z=9999
    print('Zero Division was avoided, 9999 was passed instead')
finally:    
    print(z)
    
#%%
# If no exception is listed in the except statement it runs the code if ANY 
# exception happens
x = 3
y = 0
try:
    z=x/y
    print('No Zero Division Found')
except:
    z=9999
    print('Zero Division was avoided, 9999 was passed instead')
finally:    
    print(z)

#%%
# We can also provide a tuple with the types of exceptions
x=3
y=0
try:
    z=x/y
except (ZeroDivisionError,TypeError,NameError):
    print('Strange Things Have Happened')
else:
    print('Everything Fine, the result is:',z)

#%%
# Raising a custom exception with raise statement
x=-1
try:
    if x<0:
        raise ValueError('Are you tripping? This number is negative')
except ValueError as e:
    print(e)
