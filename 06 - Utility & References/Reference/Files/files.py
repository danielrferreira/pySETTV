#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 11:30:28 2023

@author: danielferreira
"""

# This code contains examples to open, read and write external files

#%%
#Open file with open() 
#open(file[,access_mode][,buffer_value])
clash = open('input.txt','r')

#%%
#While the text file is open, you can use other functions to read or write
text = clash.read()

#%%
#It is always a good practice to close the file after doing what you want
clash.close()
text = clash.read() #Error since the file is closed

#%%
#Access Modes. r (read), w (write and creates/overwrite files), x (write and 
# create files if the file doesn't exists), r+ (read and write)
# There are more options not listed here to work on binary files or open in
# two modes

#%%
#Functions
clash = open('input.txt','r')
print(clash.name) #input.txt
print(clash.mode) #r
print(clash.closed) #False
clash.close()
print(clash.closed) #True

#%%
# with/as statement opens and autoclose after the indented code
with open('input.txt','r') as clash:
    print('nothing to see here')
print(clash.closed) #True

#%%
#read() function
print('No argument')
with open('input.txt','r') as clash:
    text1 = clash.read()
print(text1)
print('nBytes=10')
with open('input.txt','r') as clash:
    text2 = clash.read(10)
print(text2)

#%%
#readline() reads one line at a time and moves the pointer to next line (\n)
with open('input.txt','r') as clash:
    for i in [0,1,2]:
        print('Next Album')
        print(clash.readline())
        
#%%
#Writing, to write on a file we can open as 'w', 'a' or 'x'
with open('output.txt','w') as out:
    i=0
    while i<11:
        out.write(str(i))
        print('victory') #not on file, only the write function gets printed
        i+=1

#%%
#Other functions
with open('input.txt','r+') as clash:
    print(clash.tell()) #Prints the location of pointer
    print(clash.readlines()) #Prints all lines
    print(clash.tell()) #Prints the location of pointer
    print(clash.readable()) #Prints True if the object is readable
    print(clash.writable()) #Prints True if the object is readable
   
with open('output.txt','w') as clash:   
    text = ['The\n','only\n','band\n','that\n','matters\n']    
    clash.writelines(text) #Prints a list

    



























    