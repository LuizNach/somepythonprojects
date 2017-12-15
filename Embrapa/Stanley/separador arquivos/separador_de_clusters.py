# Separador de categorias em arquivos diferentes
# 
"""
Created on Thu Sep 14 10:24:02 2017

@author: Luiz Nachtigall

Analisa a saida de programa weka em que tuplas sao agrupadas em
cluters e cada tupla ganha um campo final com o numero de cluster
atribuido portanto e necessario a separacao dos cluters em arquivos
separados para possibilidade de analisa-los.
"""

fr = open("todas-escalas-segmentacao-EM.csv",'r')
fr2 = open("todas-escalas-segmentacao-EM.csv",'r')

lista_categorias = []
fr.readline()
for i in fr:
    aux = (i.rstrip().split(','))[-1]
    if aux not in lista_categorias:
        lista_categorias.append(aux)

lista_arquivos = []    
for j in range(len(lista_categorias)):
    lista_arquivos.append(open(str(lista_categorias[j].strip())+".csv",'w'))

fr2.readline()    
for i in fr2:
    
    aux = (i.rstrip().split(','))[-1]
    #print(aux,end=' ');print(i,end=' ')
    print(i,end='',file=lista_arquivos[lista_categorias.index(aux)])
    #input()