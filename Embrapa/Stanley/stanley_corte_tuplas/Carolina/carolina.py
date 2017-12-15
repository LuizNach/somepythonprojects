#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:29:14 2017

@author: b17752
"""

try:	
    fw = open('output.csv','w')
except:
    print("Erro: nao foi possivel gerar arquivo de saida")
try:
    file_name = "portfolio_agroecologia_com_outliers.csv"#input("Entre o nome do arquivo: ")
    fr2 = open(file_name, 'r')
except:
    print("Erro: nao foi possivel acessar arquivo de entrada")

freq = 18 #input("Escolha a frequencia de corte: ")
print("Tuplas repetidas aparecerao no maximo: "+str( freq) + " vezes\n"+"Arquivo output.csv sendo gerado" )

hash_arquivos = dict()

linha = fr2.readline(); cabecalho = linha;print(linha, end='', file=fw);''' pula linha de nome das colunas'''

linha = fr2.readline()

while( linha != ''):

    linha_split = linha.strip().split(',')
    if( hash_arquivos.__contains__(linha_split[0])):

        if  hash_arquivos[linha_split[0]]  <= int(freq) :
            print(linha, end='', file=fw)
        hash_arquivos[linha_split[0]] += 1
    else:
        hash_arquivos[linha_split[0]] = 1

    linha = fr2.readline()
    
    
fw.close();

fr = open("output.csv",'r')
fr3 = open("output.csv",'r')

lista_categorias = []
fr.readline()
for i in fr:
    aux = (i.rstrip().split(','))[-2]
    if aux not in lista_categorias:
        lista_categorias.append(aux)

lista_arquivos = []    
for j in range(len(lista_categorias)):
    lista_arquivos.append(open(str(lista_categorias[j].strip())+".csv",'w'))
    
for j in range(len(lista_categorias)):
    print(cabecalho,end='',file=lista_arquivos[j])

fr3.readline()    
for i in fr3:
    
    aux = (i.rstrip().split(','))[-2]
    #print(aux,end=' ');print(i,end=' ')
    print(i,end='',file=lista_arquivos[lista_categorias.index(aux)])
    #input()