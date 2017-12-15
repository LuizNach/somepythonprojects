# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

fr = open("bd-solos-modificado.csv",'r');
fw = open("bd-4grauclassificacao.csv",'w');

line = fr.readline().strip()
print(line,file=fw);
print(line);
print();

line = fr.readline().strip()
print(line);
print();

while line != "":
    line = line.split(',')
    print("Pre: ",end='')
    print(line);
    print();
    #print("linha")
    #print()
    aux = ''
    if line[-1] != '?':
        line[-1] = line[-2]+' '+line[-1]
    for i in line:
        aux += i + ','
        
    line = aux.rstrip(',')
    
     
    print("Pos: ",end='')
    print(line)
    print()
    print(str(line),file=fw)
    
    line = fr.readline().strip();


fr.close();
fw.close();