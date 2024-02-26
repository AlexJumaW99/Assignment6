#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:04:20 2024

@author: alexjuma
"""

import csv

# simple way
def read_csv(file):
    with open(file) as mydata:
        temp_sum = 0
        temp_count = 0
        
        print('*************CLIMATE DATA*************')
        for line in csv.DictReader(mydata):
            print(line)
            if line['Temp']:
                temp_sum += float(line['Temp'])
                temp_count += 1
        print('\n')
        avg_temp = temp_sum/temp_count
        print(f'The average temperature is {avg_temp}')
    
    
        


read_csv('assignment6.csv')