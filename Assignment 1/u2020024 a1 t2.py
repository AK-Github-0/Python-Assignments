# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 23:40:31 2021

@author: Abdullah Khan
"""

list ={}

with open("Input.txt", "r") as file:
    
    for line in file.read().splitlines():
        
        if line not in list:
            
            list[line] = 1
        
        else:
            
            list[line] = (list[line])+1

print("This is the data in input file : ",list)