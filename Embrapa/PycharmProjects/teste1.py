# Testing input file and parsing
#
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

f3 = open("input.in")
line3 = f3.readline().rstrip()
print("Fez f3.readline com rightStrip...diferente de f2: ", end='');print(line3.split(' '))
line3 = f3.readline().rstrip()
print("Fez o f3.readline em seguida: ", end='');print(line3.split(' '))


print()
line = f3.readline() #le uma linha vazia
line = f3.readline()
print(line.strip())
linha_list = f3.readline().strip().split(';') #mesmo fazendo o split cria-se um ultimo objeto vazio no final da lista portanto e necessario ignorar o ultimo objeto
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
print()
print("Printando no loop:")
for i in lista2[:-1]:
    print(i)

print("teste do iterator:")
x = iter(lista2)
for a in range(len(lista2)-1):
    print(next(x))

    