#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 12:51:09 2017
Programa destinado ao Stanley Oliveira
@author: Luiz Nachtigall
"""
file_name = input("Nome do arquivo do Weka: ")
file = open(file_name);

linha = file.readline().strip();#print(linha, end = '');
while( ("J48 pruned tree" not in linha) and linha != ''):
    linha = file.readline();#print(linha, end = '');
file.readline();
file.readline();
linha = file.readline();

list_conditions = [];
grade = 0;

while(linha != '\n'):    
    counter = linha.count("|   ");
    if(':' in linha):
        if(counter > grade):
            
            for i in list_conditions:
                print(i+" ",end='AND ');
            print(linha.strip('\n "|   " ').replace(':'," THEN"));
        elif counter == grade:
            if list_conditions != [] : list_conditions.pop();
                        
            for i in list_conditions:
               print(i+" ",end='AND ');
            print(linha.strip('\n "|   " ').replace(':'," THEN"));
        else:
            aux = grade - counter;
            for i in range(aux+1):
                list_conditions.pop();
            grade-=aux;
            
            for i in list_conditions:
                print(i+" ",end='AND ');
            print(linha.strip('\n "|   " ').replace(':'," THEN"));
    else:
        
        if counter > grade:
            list_conditions.append(linha.strip('\n "|   "'));
            grade+=1;
        elif counter == grade:
            if list_conditions != [] : list_conditions.pop();
            list_conditions.append(linha.strip('\n "|   " '));
        else:
            aux = grade - counter;
            
            for i in range(aux):
                list_conditions.pop();
            grade-=aux;
            list_conditions.append(linha.strip('\n "|   "'));
            
    linha = file.readline();
    
   
"""
=== Classifier model (full training set) ===

J48 pruned tree
------------------

X < 49.0
|   Y<30
|   |   Z>3 : pera
|   |   Z=2 : mamao
|   |   Z=1 : maca
|   Y>31
|   |   Z>=50 : pera
|   |   Z=49 : abacate
|   |   Z<49 : abacaxi
X = 50.0 : banana
X > 50.0
|   Z='A'
|   |   Y='K' : bergamota
|   Z='B'
|   |   Y='K' : bergamota
|   |   Y='W' : mixirica
|   Z='C' : pacoca
"""

'''    
    
=== Classifier model (full training set) ===

J48 pruned tree
------------------

petalwidth <= 0.6: Iris-setosa (50.0)
petalwidth > 0.6
|   petalwidth <= 1.7
|   |   petallength <= 4.9: Iris-versicolor (48.0/1.0)
|   |   petallength > 4.9
|   |   |   petalwidth <= 1.5: Iris-virginica (3.0)
|   |   |   petalwidth > 1.5: Iris-versicolor (3.0/1.0)
|   petalwidth > 1.7: Iris-virginica (46.0/1.0)


'''
