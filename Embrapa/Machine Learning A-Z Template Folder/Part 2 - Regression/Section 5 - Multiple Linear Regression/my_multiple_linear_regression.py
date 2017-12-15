#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 09:48:27 2017

@author: Luiz Nachtigall

Multiple Linear Regression
using backward elimination
"""



"""
All-In:
    -for some reason you have to use all...knowledge or you r told to...
    -preparing for backward eliminataion

"""

#Multiple Liner Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("50_Startups.csv")
matrizX = dataset.iloc[:,:-1].values
matrizY = dataset.iloc[:,-1].values

# Enconding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_matrizX = LabelEncoder()
matrizX[:,3] = labelencoder_matrizX.fit_transform(matrizX[:,3])

onehotencoder_matrizX = OneHotEncoder(categorical_features = [3])
matrizX = onehotencoder_matrizX.fit_transform(matrizX).toarray()

#Avoiding Dammy variable trap
"""
    evitar uma variavel dummy para nao haver dependencias redundantes
"""
matrizX = matrizX[:,1:]

#Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
matrizX_train, matrizX_test, matrizY_train, matrizY_test = train_test_split(matrizX, matrizY, test_size = 0.2, random_state = 0)

#Feature Scaling
'''
    the library take care of the scaling, no need to do it manually
'''

# Fitting Multiple Linear Regression to the Trainind Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(matrizX_train,matrizY_train)

# Prediction the Test set results
matrizY_predicted = regressor.predict(matrizX_test)

# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
'''por algum motivo o stats precisa adicionar uma coluna para q ele interprete a equacao como  y = b0*1 + b1*x1 + b2*x2 + ... '''
matrizX = np.append( arr = np.ones((50,1)), values = matrizX, axis = 1 )
""" Backward Elimination """
matrizX_optimal = matrizX[:,[0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS( endog = matrizY, exog = matrizX_optimal ).fit()
regressor_OLS.summary()

matrizX_optimal = matrizX[:,[0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS( endog = matrizY, exog = matrizX_optimal ).fit()
regressor_OLS.summary()

matrizX_optimal = matrizX[:,[0, 3, 4, 5]]
regressor_OLS = sm.OLS( endog = matrizY, exog = matrizX_optimal ).fit()
regressor_OLS.summary()

matrizX_optimal = matrizX[:,[0, 3, 5]]
regressor_OLS = sm.OLS( endog = matrizY, exog = matrizX_optimal ).fit()
regressor_OLS.summary()
