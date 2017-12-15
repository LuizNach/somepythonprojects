"""
input file and parsing
"""
#---------------------------------------------------------------------------------
f = open("input.in",'r')

'''
line = f.read()
#print("Fez o f.read: ", end='');print(line.split(' '))
line = f.readline()
print("Fez o f.readline depois do read(achou EOF): ", end='');print(line.split(' '))
print('')
'''
'''
f2 = open("input.in")
line2 = f2.readline()
print("Do inicio, fez um f2.readline: ", end=''); print(line2.split(' '))
line2 = f2.readline()
print("Fez o f2.readline em seguida: ", end=''); print(line2.split(' '))
print('')
'''
#---------------------------------------------------------------------------------
'''
f3 = open("input.in")
line3 = f3.readline().rstrip()
print("Fez f3.readline com rightStrip...diferente de f2: ", end='');print(line3.split(' '))
line3 = f3.readline().rstrip()
print("Fez o f3.readline em seguida: ", end='');print(line3.split(' '))


print()
line = f3.readline()
line = f3.readline()
print(line.strip())
linha_list = f3.readline().strip().split(';') #se nao der strip antes do split o ultimo elemento da lista sera um '\n'...como o strip vem antes o ultimo elemento da lista e vazio
print(linha_list)

lista2 = []
for i in linha_list:
    lista2.append(i.strip('\'\"'))
print(lista2)

lista2 = []
for i in linha_list:
    lista2.append(i.strip('\'\" null  '))
print(lista2)

print(lista2[:-1])
'''
#---------------------------------------------------------------------------------
"printing formatted float value with 2 decimal places" '''
print("I have %f" % 45)
print("I have {0:.1f}".format(42))
print("I have {0:.10f}".format(42))
print("Favorite number is %d" % 42)
a = int(input("Entre o valor de a por exemplo {0:d}:".format(5) ))
print("This is a fomatted 6 espaces number: %6d" % a)
print("This is a fomatted 6 zeros number: %06d" % a)
b = int(input("Entre o valor de b por exemplo {0:f}:".format(10)))
print("Simple output 2 variables: %d %d" % (a, b) ,"bla")
print("Simple output 2 variables:",a, b,"aqui toda vez q vc coloca uma var nova, ocorre um espacamento");
print("first number {0:d}, second number {0:.2f}".format(a,b))
print("first broken command: "+ \
      "{0:d} second number on broken command: {1:d}".format(a,b) , "o barra invertida permite o compilador entender que o comando continua na proxima linha");
'''
#---------------------------------------------------------------------------------
'''
import datetime
data_de_hoje = datetime.date.today()
print(data_de_hoje,end='');print(" year, month , day")
print(data_de_hoje.year)
print(data_de_hoje.month)
print(data_de_hoje.day)
#strftime string from time allows you to specify the date format, look at github
print(data_de_hoje.strftime('%d %b %Y')) #mes abreviado e ano com 4 dig
print(data_de_hoje.strftime('%d %B %y')) #mes completo e ano com 2 dig
print(data_de_hoje.strftime("Please attend our event %A, %B %d in the year %Y"))
#procurar como localizar datas babel.pocoo.org para mudar datas e moedas
birthday = input("Whats your birthday?")
birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
print(birthday)
'''
#---------------------------------------------------------------------------------
"""
    resolvi criar uma matriz nula 10x10
"""
matriz = list()
for i in range(10):
    matriz.append(list())
for i in range(10):
    for j in range(10):
        matriz[i].append(0)

print(matriz)

for i in range(10):
    for j in range(10):
        print(matriz[i][j],end='')
    print()