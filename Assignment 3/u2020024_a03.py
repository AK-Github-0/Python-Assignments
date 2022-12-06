# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:00:08 2021

@author: Abdullah Khan(2020024)
"""

class MyVector:
    
    def __init__(self, *args):
        
        for x in args:
        
            if type(x)==int:
            
                self.args=args
            
            else:
            
                raise ValueError
                
        self.args = list(args)
    
    def __str__(self):
    
        return str(tuple(self.args))
    
    def __len__(self):
        
        return len(self.args)
    
    def __add__(self, other):
        
        if len(self.args) == len(other.args):
        
            l = []
            
            for i in range(len(self.args)):
            
                l.append(self.args[i] + other.args[i])
            
            return MyVector(*l)
        
        else:
            
            print("Vectors are not equal")
    
    def __getitem__(self,x):
        
        if x > len(self.args):
        
            return
        
        else:
        
            return self.args[x]
        
    def __setitem__(self,x,y):
        
        if x > len(self.args):
        
            return
        
        else:
        
            return self.args[x+y]
    
    def __abs__(self):
        
        abs_arg = 0
        
        for index in self.args:
        
            abs_arg = abs_arg + index**2
        
        abs_arg = abs_arg**0.5
        
        return abs_arg
    
    def __bool__(self):
        
        abs_arg = abs(self)
        
        if len(self.args) <= 0 or abs_arg < 0:
            
            return False
        
        else:
        
            return True
    
    def __mul__(self, Const):
        
        if type(Const) == int:
        
            Mul = []
            
            for x in self.args:
            
                Mul.append(x*Const)
            
            return MyVector(*Mul)
        
        else:
        
            print("Wrong format Salar Mutiplication only allowed")
    
    def __lshift__(self, Turns):
        
        l1 = self.args 
        
        for Rotation in range(Turns,0,-1):
        
            Temp = l1[0]
            
            for x in range(len(l1) - 1):
            
                l1[x] = l1[x+1]
            
            l1[len(l1)-1] = Temp
        
        return MyVector(*l1)


A1 = MyVector(2,4,7,8)

A0 = MyVector()
print(A0)

print("The elements in A1 are",A1)
print(len(A1))

A2 = MyVector(1,2,3,4)

#Iterating object
for x in A1:
    print(x)
print(A1[2])

for x in A2:
    print(x)

#Scalar Multiplication
A3= A1*3
print(A3)

#Rotating elements
A4 = MyVector(2,3,4,5)
A4= A2<<1
print(A4)
