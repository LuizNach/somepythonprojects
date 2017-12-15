#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 12:51:09 2017
Programa destinado ao Stanley Oliveira
@author: Luiz Nachtigall

input: arquivos de dados em formato rtf

output: arquivo unico contendo todas as tuplas com os respectivos campos preechidos
"""

import os
'''path = os.getcwd()'''

def list_my_directories():
    list_of_dir = [x for x in os.listdir('.') if x.startswith("Perfis")]
    return list_of_dir

print(list_my_directories())
print(len(list_my_directories()))