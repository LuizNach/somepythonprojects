# Tuplas aletarias selecionadas sem repeticao
"""
Created on Wed Sep 13 11:50:18 2017
@author: Luiz Nachtigall
"""
"""
- Pequena 6464 (1616) - 25%
- Média - 1489 - sem restrição - só repete no arquivo final
- Grande 3511 (1404) - 40%
- Tentar gerar as instâncias de forma aleatória, sem repetição.
"""
import random
def main():
    try:
        fw = open("CUT_Portfolio_todas_regioes_ordenado_.csv",'w')
    except:
        print("Erro: nao foi possivel gerar arquivo de saida")
    try:
        fr = open("Portfolio_todas_regioes_ordenado_por_escala.csv",'r')
    except:
        print("Erro: nao foi possivel acessar arquivo de entrada")
    
    
    #result = list()
    lista = list()
    tupla = fr.readline()
    print(tupla,end='',file=fw)
    
    for i in range(6464):
        tupla = fr.readline()
        lista.append(tupla)
    #print("Pequenos: "+str(len(lista)))
    #lista2 = list()
    for i in range(1616):
        rdm = random.randrange(len(lista))
        print(lista[rdm],end='',file = fw)
        #lista2.append(lista[rdm])
        #result.append(lista[rdm])
        del lista[rdm]
        """ talvez falte retirar a quebra de linha aqui"""
    #print("Pequenos2: "+str(len(lista2)))
    for i in range(1489):
        tupla = fr.readline()
        print(tupla,end='',file = fw)    
        #result.append(tupla)
    lista3 = list()
        
    for i in range(3511):
        tupla = fr.readline()
        lista3.append(tupla)
    #print("Grandes: "+str(len(lista3)))
    #lista4 = list()
    for i in range(1404):
        rdm = random.randrange(len(lista3))
        print(lista3[rdm],end='',file = fw)
        #lista4.append(lista3[rdm])
        #result.append(lista3[rdm])
        del lista3[rdm]
    #print("Grandes2: "+str(len(lista4)))
    print("Programa gerou o arquivo de saida: CUT_Portfolio_todas_regioes_ordenado_")

if __name__ == "__main__":
    main()