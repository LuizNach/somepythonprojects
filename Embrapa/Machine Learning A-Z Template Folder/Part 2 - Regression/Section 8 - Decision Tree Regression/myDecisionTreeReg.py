#Decision Tree Regression
"""
Created on Mon Sep  4 14:53:31 2017
@author: Luiz Nachtigall
"""
#Librarys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Reading files with pandas
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:-1].values
Y = dataset.iloc[:, -1].values

#Splittin the dataset into Training set and Test set

#Featuring Scaling

#Fitting the Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, Y)

# Predicting a new result
Y_pred = regressor.predict(6,5)

#Visualisation com poucos pontos ocorre uma inducao erronea no grafico
plt.scatter(X,Y,color = 'red')
plt.plot(X, regressor.predict(X),color = 'blue')
plt.title("Decision Tree Regression (somente dados)")
plt.xlabel("Time Exp (years)")
plt.ylabel("Salary ($Dollar)")
plt.show()

#Visualisation Tree com a precisao correta

plt.scatter(X,Y,color = 'red')
X_grid = np.arange(min(X),max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.plot(X_grid, regressor.predict(X_grid),color = 'blue')
plt.title("Decision Tree Regression (comportamento no intervalo)")
plt.xlabel("Time Exp (years)")
plt.ylabel("Salary ($Dollar)")
plt.show()
