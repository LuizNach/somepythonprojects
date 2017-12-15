#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:16:44 2017

@author: b17752
"""


class meuobjeto():
    def __init__(self, a, b, c):
        self.atrib1 = a
        self.atrib2 = b
        self.atrib3 = c

    def __str__(self):
        this_str = "meu objeto: ";
        this_str += 'atrb1: ' + str(self.atrib1) + ' ';
        this_str += 'atrb2: ' + str(self.atrib2) + ' ';
        this_str += 'atrb3: ' + str(self.atrib3) + ' ';
        return this_str;


lista = []

for i in range(5):
    lista.append(meuobjeto(0, 1, i))
for i in range(5):
    lista.append(meuobjeto(1, i, 3))
for i in range(5):
    lista.append(meuobjeto(2, 3, 4))

print("LISTA ANTES: ")
for i in lista:
    print(i)

lista2 = list()
for i in lista:
    if i.atrib1 == 1:
        # print("achou")

        lista2.append(i)
        # lista.remove(i)

print("LISTA DEPOIS: ")
for i in lista:
    print(i)

print("LISTA 2")
for i in lista2:
    print(i)

print("--------------------------------------------------")

lista2[0].atrib1 = 9;
lista2[1].atrib1 = 9;
lista2[2].atrib1 = 9;
lista2[3].atrib1 = 9;
lista2[4].atrib1 = 9;

print("LISTA DEPOIS: ")
for i in lista:
    print(i)

print("LISTA 2")
for i in lista2:
    print(i)

print("--------------FINAL------------------------------------")

for i in lista2:
    # lista.remove(i)
    pass

print("LISTA DEPOIS: ")
for i in lista:
    print(i)

print("LISTA 2")
for i in lista2:
    print(i)