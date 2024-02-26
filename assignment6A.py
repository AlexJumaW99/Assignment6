#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:27:46 2024

1. Using your favourite text editor, create a text file containing these lines:

Amethyst #9966cc
Apricot #fbceb1
Aqua #00ffff
Blond #faf0be

2. Write a function that reads the text file into a string, one line at a time, and looks for the line containing the word “Aqua”, and replaces that line with:

Azure #007fff

3. Write another function to overwrite the original file with the modified text, so the original file looks like:

Amethyst #9966cc
Apricot #fbceb1
Azure #007fff
Blond #faf0be

@author: alexjuma
"""

'''
myfile = open('assignment6.txt', 'r')
print(myfile.read())

myfile.close()
'''

#It's easier to use the file context manager because it closes the file
#automatically after use
def text_to_string(file):
    with open(file, 'r') as myfile:
        file_string = ''
        file_lines = myfile.readlines()
        for line in file_lines:
            file_string += line
        
        print('The original file string contains:')
        print(file_string,'\n')
        
        file_string = file_string.replace('Aqua #00ffff', 'Azure #007fff')
        
        print('The new file string contains:')
        print(file_string)
        

text_to_string('assignment6.txt')

def overwrite_file(file):
    with open(file, 'w+') as myfile:
        myfile.write('Amethyst #9966cc\n')
        myfile.write('Apricot #fbceb1\n')
        myfile.write('Azure #007fff\n')
        myfile.write('Blond #faf0be')
        
        print(myfile.read())
        
overwrite_file('assignment6.txt')
            
    
    
    
    
    