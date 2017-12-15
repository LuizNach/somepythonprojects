#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:14:40 2017

@author: Luiz Nachtigall
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing data
dataset =pd.read_csv("Position_Salaries.csv")
matrizX = dataset.iloc[:,1:2].values
matrizY = dataset.iloc[:,-1].values

#Splitting the data set
'''from sklearn.cross_validation import train_test_split
matrizX_train, matrizX_test, matrizY_train, matrizY_test = train_test_split(matrizX,matrizY, test_size = 0.2, random_state =0)'''

#Feature Scaling
'''
from sklearn.preprocessing import StandardScaler
sc_matrizX = StandardScaler()
matrizX_train = sc_matrizX.fit_transform(matrizX_train)
matrizX_test = sc_X.transform(matrizX_test)

'''

#Fitting Linear Regression to the data set
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(matrizX,matrizY); ''' criar coeficientes da linha que melhor se adequa a esses pontos'''

#Fitting Polynomial Regression to the data set
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4); ''' cria o objeto com parametro de polinomio de 4 grau'''
matrizX_poly = poly_reg.fit_transform(matrizX); ''' usa o metodo conversor de matriz nx1 no objeto LinearRegression para que ele entenda q sera uma regressao polinomial, na verdade regressao multilinear'''

lin_reg2 = LinearRegression() 
lin_reg2.fit(matrizX_poly,matrizY); ''' fara uma regressao multilenar usando a matriz que representa as variaveis em potencias para cada coluna, com coeficientes a determinar'''

#Visualising the Linear Regreesin results
plt.scatter(matrizX,matrizY,color="red")
plt.plot(matrizX, lin_reg.predict(matrizX) , color = "blue"); ''' o predict retorna a lista com os coeficientes para a adequacao linear, entao faz a melhor reta com o input matrizX'''
plt.title("Truth or bluff? Linear Regression")
plt.xlabel("Position Level")
plt.ylabel("Time of experience")
plt.show()
#Visualising the Polynomial Regreesion results
plt.scatter(matrizX,matrizY,color="red")
plt.plot(matrizX, lin_reg2.predict(poly_reg.fit_transform(matrizX)) , color = "green"); ''' o predict retorna a lista com os coeficientes para a adequacao polinomial'''
plt.title("The Polynomial Regression")
plt.xlabel("Position Level")
plt.ylabel("Time of experience")
plt.show()

X_grid = np.arange( min(matrizX), max(matrizX), 0.1); ''' matriz grid possui'''
X_grid = X_grid.reshape( (len(X_grid), 1) )
plt.scatter(matrizX,matrizY,color = 'red')
plt.plot(X_grid,lin_reg2.predict(poly_reg.fit_transform(X_grid)),color="orange")
plt.title("Poly Reg com precisao no polinomio")
plt.xlabel("Position Level")
plt.ylabel("Time of experience")
plt.show()

#Predicting a new result with Linear Regression
lin_reg.predict(6.5)

# Predicting a new result with Polynomial Regression
lin_reg2.predict(poly_reg.fit_transform(6.5))