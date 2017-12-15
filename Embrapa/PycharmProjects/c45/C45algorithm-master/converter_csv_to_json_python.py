
try:
    fw = open('table2.json','w')
except:
    print("Fail to create output file\n")
try:
    fr = open('../C45_input_iris_csv.csv','r')

    fw.write('{\n')
    results = fr.readline().strip().split(',')
    table_variaveis = list()
    for i in results:
        table_variaveis.append(list())

    linha = fr.readline().strip()
    list_ = list()
    while( linha != '' ):
        list_ = linha.split(',')
        for j in range(0,len(list_)):
            table_variaveis[j].append(list_[j])
        linha = fr.readline().strip()

    for i in range(-1,len(table_variaveis)-1):
        print("\t\""+str(results[i])+"\": ", end='',file=fw)
        print(table_variaveis[i],end='',file=fw)
        print(",",file=fw)

    print('}', end='\n', file=fw)
    """maneira diferente de printar em arquivo com varios parametros"""

except:
    print("Deu pau")