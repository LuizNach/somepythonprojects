"""
Programa que corta tuplas com frequencia maior que estabelecido, saida e o csv output

"""

def main():

    try:
        fw = open("output.csv",'w')
    except:
        print("Erro: nao foi possivel gerar arquivo de saida")
    try:
        fr = open("freqArq.csv",'r')
        fr2 = open("portfolio_Total.csv", 'r')
    except:
        print("Erro: nao foi possivel acessar arquivo de entrada")

    freq = input("Input de frequencia: ")
    print("Frequencia escolhida: "+str( freq) + " arquivo  de saida sendo gerado" )

    hash_arquivos = dict()
    linha = fr.readline()
    linha = fr.readline()
    while(linha != ''):

        linha_split = linha.strip().split(',')
        hash_arquivos[ linha_split[0] ] = linha_split[1]
        linha = fr.readline()

    linha = fr2.readline()
    linha = fr2.readline()
    while( linha != ''):

        linha_split = linha.strip().split(',')

        if( int(hash_arquivos[linha_split[0]]) <= int(freq) ):
            print(linha,end='',file=fw)
        linha = fr2.readline()


if __name__ == "__main__":
    main()