# Data Preprocessing
"""
Created on Mon Jul 31 09:19:17 2017

@author: Luiz Nachtigall
"""

#Imported Libraries
"""
Numpy for mathematical functions
MatPlotLib for interface ploting
Pandas for import and manage data sets
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing dataset
dataset = pd.read_csv('Data.csv')

'''
matriz recebera so os valores de iloc[todas_as_linhas;colunas_ate_a_penultima]
'''
matrizX = dataset.iloc[:,:-1].values 
matrizY = dataset.iloc[:,-1].values 

# Take care of missing data
# do scikit learn importamos o imputer que faz onde houver  variaveis vazias,criase uma media das outras para nao influenciar na analise
# o imputer tem um metodo que trata dados faltantes
''' strategy=mean quer dizer que faz a media dos valores axis = 0 faz a media entre as colunas, axis = 1 faz a media entre as linhas '''
''' passando so os campos da matriz que podem ser contabilizados para substituir NaN'''
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(matrizX[:,1:])
matrizX[:,1:] = imputer.transform(matrizX[:,1:])    

# Enconding categorical data
'''
    o encoder faz o seguinte: ele pega uma coluna que seus atributo e uma categoria e atribui valores para isso
'''
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_matrizX = LabelEncoder()
matrizX[:,0] = labelencoder_matrizX.fit_transform(matrizX[:,0])