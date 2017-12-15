# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:31:05 2017

@author:Luiz Nachtigall
"""

"""
Primeiro programa com logistic regression
Capitulo de prediscao de classificacao
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:,[2,3]].values ; # escolhemos somente as colunas de idade e salario para saber se influenciam na compra do produto
Y = dataset.iloc[:,-1].values; # ultima colunas diz se ocorreu a compra do produto

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
#na variavel Y nao ha necessidade de se fazer o scaling pois ele ja se encontra entre 0 e 1

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
conf_matrix = confusion_matrix(Y_test,Y_pred)

"""

Agora mostrar os resultados da previsao da regressao logistica linear
"""