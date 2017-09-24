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
O labelencoder faz o seguinte: ele pega uma coluna que seus atributo e uma categoria e atribui valores discretos para os elementos
O onehotencoder
'''
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_matrizX = LabelEncoder()
matrizX[:,0] = labelencoder_matrizX.fit_transform(matrizX[:,0])

onehotencoder_matrizX = OneHotEncoder(categorical_features = [0])
matrizX = onehotencoder_matrizX.fit_transform(matrizX).toarray()

labelencoder_matrizY = LabelEncoder()
matrizY = labelencoder_matrizY.fit_transform(matrizY)

#Splitting the dataset into the Training set and Test set
'''
Bom espacamento para o campo de testes é de 20 a 25% dos seus dados
'''
from sklearn.cross_validation import train_test_split
matrizX_train, matrizX_test, matrizY_train, matrizY_test = train_test_split(matrizX, matrizY, test_size = 0.2, random_state = 0)

#Feature Scaling
'''
-O scaling faz com que se coloque as variaveis em mesma ordem de grandeza,
de maneira que nao haja uma sobre ponderação de uma var sobre outra.
-Para algoritmos que usam as variaveis como coordenadas, cada tupla um ponto 
num grafico de n dimensoes, os saltos sao feitos com ponderacao das distancias 
entre eles portanto se nao houver um nivelamento entre as variaveis, algumas 
delas serao desconsideradas pois nao afetam a distancia euclidiana.
'''
from sklearn.preprocessing import StandardScaler
scaling_X = StandardScaler()
matrizX_train = scaling_X.fit_transform(matrizX_train)
matrizX_test = scaling_X.transform(matrizX_test)
"""
por algum motivo quando se faz o fit, fica na construção do objeto os moldes da matriz...
como o train e o test possuem mesmo formato, na segunda chamada so se usa o transform...
economizando tempo
"""