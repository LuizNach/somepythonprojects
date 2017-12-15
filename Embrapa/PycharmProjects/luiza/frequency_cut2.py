"""
input: Arquivo.csv 
output: output.csv
Programa que corta tuplas quando a frequencia supera o estabelecido
criterio de observacao e o primeiro campo
output e um arquivo csv com as tuplas aparecendo um numero de vezes no maximo da frequencia estabelecida
segue a ordem dos elementos do arquivo de entrada

"""

def main():

    try:
	
        fw = open('output.csv','w')
    except:
        print("Erro: nao foi possivel gerar arquivo de saida")
    try:
        file_name = input("Entre o nome do arquivo: ")
        fr2 = open(file_name, 'r')
    except:
        print("Erro: nao foi possivel acessar arquivo de entrada")

    freq = input("Escolha a frequencia de corte: ")
    print("Tuplas repetidas aparecerao no maximo: "+str( freq) + " vezes\n"+"Arquivo output.csv sendo gerado" )

    hash_arquivos = dict()

    linha = fr2.readline(); ''' pula linha de nome das colunas'''
    
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
    

if __name__ == "__main__":
    main()
