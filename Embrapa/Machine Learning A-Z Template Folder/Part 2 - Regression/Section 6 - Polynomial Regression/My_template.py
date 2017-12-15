#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:00:28 2017

@author: Luiz Nachtigall
"""

import pandas as pd
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:,1:-1].values
Y = dataset.iloc[:,-1:].values

#Splitting the dataset into the Training and Test set

#Feature Scaling

#Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
''' criar o conversor que serve para setar qual grau do poli e criar uma matriz de multiplas var para os expoentes com matriz de entrada'''
conversor_polinomial = PolynomialFeatures(degree = 4);
matriz_var_poly = conversor_polinomial.fit_transform(X);
#conversor_polinomial.fit(matriz_var_poly,Y)
linear_regression = LinearRegression()
linear_regression.fit(matriz_var_poly, Y)

#For higher resolution at the graph
import numpy as np
dominio_X = np.arange(min(X),max(X),0.1)
dominio_X = dominio_X.reshape(len(dominio_X),1)

import matplotlib.pyplot as plt
plt.scatter(X,Y,color='red')
plt.plot(dominio_X,linear_regression.predict(conversor_polinomial.fit_transform(dominio_X)),color='blue')
plt.show()

print( linear_regression.predict(conversor_polinomial.fit_transform([[6.5]])) )