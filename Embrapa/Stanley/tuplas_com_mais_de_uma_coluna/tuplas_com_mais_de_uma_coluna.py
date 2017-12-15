# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:39:34 2017

@author: Luiz Nach
"""

file_name = input("Entre com o nome do arquivo: ")

fr = open(file_name,'r')
fw = open("output.csv",'w')
print(fr.readline(),file=fw)
line = fr.readline()
while line != "" :
    if line.find(',') :
        print(line)
        print(line,file=fw)
    line = fr.readline()
