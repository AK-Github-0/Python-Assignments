# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 23:49:11 2021

@author: Abdullah Khan
"""
file = open("input.txt","r")

print("Input file has opened ")

print(file.read())

file.close()

print("Input file is closed")