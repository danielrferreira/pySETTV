#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:18:00 2023

@author: danielferreira
"""

#%%
# Functions: 
def remove_special_chars(text, sc='[~!@#$%^&*+-:,<>?]',rp='_'):
    '''This function will replace special characters listed on sc and replace with the rp character (default parameters: sc=[~!@#$%^&*+-:,<>?] rp=_'''
    from re import sub
    return sub(sc,rp,text)
    
def truncate(text,max=32):
    '''This function will truncate a text to maximun length (default: max=32)'''
    if len(text)>max:
        return text[0:max-1]
    else:
        return text
    
def number_first(text):
    '''This function will replace the first character to _ if first character is a number'''
    if text[0] in [str(x) for x in range(9)]:
        return '_'+text[1:len(text)]
    else:
        return text

def cleaning_strings(text,oper):
    '''This function will do all operations listed on clean_ops to the text'''
    for func in oper:
        text = func(text)
    return text
#%%
# Example of usage:
# First you need to list each one of the functions you need in the clean_ops variable:
clean_ops = [remove_special_chars,truncate,number_first, str.strip,str.title]
# example of string list you could apply the master function:
strings = ['askdjhakjsdn,am xajsnkjassdjfhskjdhfkjsdhfkjshdfjkhdf','  Daskks', '%Xbsdkk&', '8_dezena', 'Das%%2']
for i,text in enumerate(strings):
    strings[i]=cleaning_strings(strings[i],clean_ops)
print(strings)  
#%%
