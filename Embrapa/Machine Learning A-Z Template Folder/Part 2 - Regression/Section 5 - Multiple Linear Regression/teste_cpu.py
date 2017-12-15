#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 14:43:41 2017

@author: Luiz Nachtigall

Multiple Linear Regression - Using Backward Elimination
"""

#Multiple Liner Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("cpu.csv")
matrizX = dataset.iloc[:,:-1].values
matrizY = dataset.iloc[:,-1].values

# Enconding categorical data


"""
    evitar uma variavel dummy para nao haver dependencias redundantes
"""
lista = list()
lista2 = list()
for i in range(10):
#Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    matrizX_train, matrizX_test, matrizY_train, matrizY_test = train_test_split(matrizX, matrizY, test_size = 0.3, random_state = i)
    
    #Feature Scaling
    
    # Fitting Multiple Linear Regression to the Trainind Set
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor = regressor.fit(matrizX_train,matrizY_train)
    
    # Prediction the Test set results
    matrizY_predicted = regressor.predict(matrizX_test)
    
    # Building the optimal model using Backward Elimination
    import statsmodels.formula.api as sm
    '''por algum motivo o stats precisa adicionar uma coluna para q ele interprete a equacao como  y = b0*1 + b1*x1 + b2*x2 + ... '''
    matrizX = np.append( arr = np.ones(( len(matrizX[:,0] ),1)), values = matrizX, axis = 1 )
    """ Backward Elimination """
    matrizX_optimal = matrizX[:,[0, 1, 2, 3, 4, 5, 6]]
    regressor_OLS = sm.OLS( endog = matrizY, exog = matrizX_optimal ).fit()
    #regressor_OLS.summary()
    
    matrizX_optimal = matrizX[:,[0, 1, 2, 3, 4, 6]]
    regressor_OLS = sm.OLS( endog = matrizY, exog = matrizX_optimal ).fit()
    #regressor_OLS.summary()
    
    '''
    Spearman's rank correlation coefficient http://www.mathsisfun.com/data/correlation.html
    '''
    from scipy.stats.stats import spearmanr
    lista2.append(spearmanr(matrizY_predicted,matrizY_test)[0])
    from scipy.stats.stats import pearsonr
    lista.append(pearsonr(matrizY_predicted,matrizY_test)[0] )

#print((0.95190710169581816+0.86696317429723413+0.96413387723710764+0.94513629805376798+0.92383078388034234+0.88246447537053851+0.85531845466734868+0.95957928263085779+0.91597753673971671+0.8902045120622698)/10)
print("Pearson: ");print(sum(lista)/len(lista))
print("Spearman: ");print(sum(lista2)/len(lista2))