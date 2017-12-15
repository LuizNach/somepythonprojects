"""
Created on Wed Aug 30 15:10:08 2017
@author: LuizNach
"""
#SVR

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the data set
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:-1].values
Y = dataset.iloc[:,-1].values

#Splitting the dataset into Training and Test

#Feature Scaling
''' SVR nao faz feature scaling , tem q colocar eles em porcentagens adequadas a modelagem para algumas coisas nao ponderarem mais q outras'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X = sc_X.fit_transform(X)
Y = sc_Y.fit_transform(Y)

#Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X,Y)

#Predicting a new result
''' o inverse transform tira da modelagem percentual'''
Y_pred = sc_Y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))

#Visualising the SVR results
#plt.scatter(X, Y , color = 'red')
#plt.plot(X, regressor.predict(X),color = 'blue')

plt.title('Avaliacao Salarial (SVR)')
plt.xlabel('Nivel empresarial')
plt.ylabel('Salario')

plt.scatter(X, Y , color = 'red')
X_grid = np.arange( min(X), max(X), 0.1); ''' matriz grid possui'''
X_grid = X_grid.reshape( (len(X_grid), 1) )
plt.plot(X_grid, regressor.predict(X_grid),color = 'blue')

plt.scatter(sc_X.transform(np.array([[6.5]])),regressor.predict(sc_X.transform(np.array([[6.5]]))),color = 'black')

plt.show()

print("Salario previsto: "+str(Y_pred[0]))