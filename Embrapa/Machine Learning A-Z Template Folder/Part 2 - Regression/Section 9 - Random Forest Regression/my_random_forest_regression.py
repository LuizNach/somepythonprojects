# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:01:39 2017

@author: Luiz Nachtigall
"""
# Importar as bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar o conjunto de dados
dataset = pd.read_csv('Position_Salaries.csv'); #dataset sera um objeto dataFrame , um objeto matriz 2d com linhas e colunas heterogeneas,ja otimizadas para o tamanho do dado
X = dataset.iloc[:,1:-1].values ; #iloc faz o slice do data frame
Y = dataset.iloc[:,-1].values ; #resultados sao sempre alocados na ultima colunas

# Pulamos a parte de dividir em grupo de train e predict pois conjunto de dados e pequeno
'''
from sklearn.cross_validation import train_test_split
X_train , X_teste, Y_train, Y_test = train_test_split( X, Y, teste_size = 0.2, random_state = 0)
'''

#Pulamos o feature scaling
'''
from sklearn.preprocessing import StandardScaler

scaler_X = StandardScaler()
X_train = scaler_X.fit_transform(X_train)
X_test = scaler_X.transform(X_train)

scaler_Y = StandardScaler()
Y_train = scaler_Y.fit_transform(Y_train)

'''

# Adequando o objeto random_forest_regression  ao conjunto da dados da entrada
from sklearn.ensemble import RandomForestRegressor
obj_regressor = RandomForestRegressor(n_estimators = 300, criterion = "mse", random_state = 0)
obj_regressor.fit(X, Y)

# Predizendo um novo resultado
Y_predicted = obj_regressor.predict(6.5)

#Visualizacao usando os proprios pontos
plt.scatter(X, Y, color = 'red')
plt.plot(X, obj_regressor.predict(X), color = 'blue')
plt.title(" usando os proprios pontos - Random Forest")
plt.xlabel('level')
plt.ylabel('salario')
plt.show()

#Visualizacao com maior resolucao para que se possa diferenciar as tomadas de decisao
X_continuo = np.arange(min(X), max(X), 0.001)
X_continuo = X_continuo.reshape( (len(X_continuo), 1) )

plt.scatter(X, Y, color ='red')
plt.plot( X_continuo, obj_regressor.predict(X_continuo), color = 'blue')

plt.title(" Candidato - Random Forest - High definition ")
plt.xlabel("level")
plt.ylabel("salario")
plt.show()

#obj_regressor.estimators_
#obj_regressor.decision_path(X)
#obj_regressor.get_params()
#obj_regressor.predict(X)