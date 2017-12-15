def fib(n):
    a, b = 0 ,1
    lista = list()
    while a < n :
         lista.append(a)
         #lista.append(b)
         a, b = b , a+b
    return lista

print(fib(100))