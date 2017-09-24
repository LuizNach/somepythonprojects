# Data Preprocessing
"""
Created on Mon Aug 3
@author: Luiz Nachtigall
"""

#Imported Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing dataset
dataset = pd.read_csv('Salary_Data.csv')

matrizX = dataset.iloc[:,:-1].values; """ coluna de anos de experiencia """
matrizY = dataset.iloc[:,-1].values; """ coluna de salarios"""

# Take care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(matrizX[:,:])
matrizX[:,:] = imputer.transform(matrizX[:,:])    

# Enconding categorical data

#Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
matrizX_train, matrizX_test, matrizY_train, matrizY_test = train_test_split(matrizX, matrizY, test_size = 1/3, random_state = 0)

#Feature Scaling
"""
    Na linear regression, a biblioteca ja estabiliza os dados caso eles sejam desparelhos
from sklearn.preprocessing import StandardScaler
scaling_X = StandardScaler()
matrizX_train = scaling_X.fit_transform(matrizX_train)
matrizX_test = scaling_X.transform(matrizX_test)
"""

#Fitting Simple Linear Regression to the Training set
""" a biblioteca possui um metodo que cria um objeto para tratar regressao linear """
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(matrizX_train,matrizY_train)

#Predicting the Test set results￼
matrizY_predicted =regressor.predict(matrizX_test)

#Visualisation the Training set results
plt.scatter(matrizX_train, matrizY_train, color = 'red')
plt.plot(matrizX_train, regressor.predict(matrizX_train), color = 'blue')
plt.title('Salary x Experience (Training set)')
plt.xlabel('Experience (years)')
plt.ylabel('Salary (dollars)')
plt.show()

#Second graph, viasualising tests
plt.scatter(matrizX_test, matrizY_test, color = 'red')
plt.plot(matrizX_train, regressor.predict(matrizX_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Experience (years)')
plt.ylabel('Salary ($)')
plt.show()