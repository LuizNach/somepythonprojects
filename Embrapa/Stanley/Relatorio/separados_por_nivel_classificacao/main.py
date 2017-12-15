# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:33:05 2017

@author: Luiz Nachtigall
"""

fr = open("bd-solos.csv",'r')
fw1 = open("1nivelcategorico.csv",'w')
fw2 = open("2nivelcategorico.csv",'w')
fw3 = open("3nivelcategorico.csv",'w')
fw4 = open("4nivelcategorico.csv",'w')
fw5 = open("comproblema.csv",'w')

line = fr.readline()
print(line,file=fw1,end='')
print(line,file=fw2,end='')
print(line,file=fw3,end='')
print(line,file=fw4,end='')
print(line,file=fw5,end='')

line = fr.readline()
while line!= "":
    mylist = line.strip().split(',')
    if mylist[-1] != '?' and len(mylist)==102:
        print(line,file=fw4,end='')
    elif mylist[-1] == '?' and mylist[-2] != '?' and len(mylist)==102:
        print(line,file=fw3,end='')
    elif mylist[-2] == '?' and mylist[-3] != '?' and len(mylist)==102:
        print(line,file=fw2,end='')
    elif mylist[-3] == '?' and mylist[-4] != '?' and len(mylist)==102:
        print(line,file=fw1,end='')
    else:
        print(line,file=fw5,end='')
    line = fr.readline()

fr.close();#25702
fw1.close();#3391
fw2.close();#9116
fw3.close();#5326
fw4.close();#7440
fw5.close();#429