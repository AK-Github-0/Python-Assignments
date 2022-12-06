# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:56:16 2021

@author: Abdullah Khan(20202024)
"""
def Count_DNA_2(DNA_Sequence):
    
    DNA_dictionary={}
    
    DNA_list=[]
    
    i=0
    j=2
    
    size=len(DS)-1
    
    for k in range(size):
        
        l=(DNA_Sequence[i:j])
        
        i+=1
        j+=1
        
        DNA_list.append(l)
    
    for i in DNA_list:
        if i in DNA_dictionary:
            DNA_dictionary[i]+=1
        else:
            DNA_dictionary[i]=1
    
    return DNA_dictionary


def Count_DNA(DNA_Sequence,n):
    
    DNA_dictionary={}
    
    DNA_list=[]
    
    i=0
    
    size=n-1
    
    for k in range(size):
        
        l=(DNA_Sequence[i:n])
        
        i+=1
        n+=1
        
        DNA_list.append(l)
    
    for i in DNA_list:
        if i in DNA_dictionary:
            DNA_dictionary[i]+=1
        else:
            DNA_dictionary[i]=1
    
    return DNA_dictionary

def get_molecule_data(file_name,**kwargs):
    molecule_dictionary = {}
    filecheck = False
    try:
        names = open(file_name, 'r')
        filecheck = True
    except:
        print('File error. Either file doesn\'t exist or wrong name of file given! ')
    if(filecheck):
        i = 0
        for lines in names:
            i = i+1
            words = lines.split()
            
            try:
                if words[2] in kwargs:
                    if words[2] not in molecule_dictionary.keys():
                        molecule_dictionary[words[2]] = [(i, words[kwargs.get(words[2])-1])]
                    else:
                        molecule_dictionary[words[2]].append((i, words[kwargs.get(words[2])-1]))
            except:
                continue
    return molecule_dictionary

print(get_molecule_data('1bta.pdb', CA=7, N=7))

DS=str(input("Enter DNA String :"))

print("DNA String :",DS)

print(Count_DNA_2(DS))

DS=str(input("Enter DNA String :"))

print("DNA String :",DS)

n=int(input("Enter letter sequence:"))

print("Letter Sequence :",n)

print(Count_DNA(DS,n))

file_name = str(input("Enter the file name : "))

get_molecule_data(file_name, CA=7, N=7)

