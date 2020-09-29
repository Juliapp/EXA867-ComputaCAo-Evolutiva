import pandas as pd
import numpy as np
import math as mt
import random as rd

#valor de a, constante
a = 1

#equação para gerar o valor de y
def formula(x, a):
    p = (a ** 3) * (a + (2 * x))
    s = 2 * (mt.sqrt(p))
    t = s + (2 * (a ** 2)) + (2 * a * x) - (x ** 2)
    y = mt.sqrt(abs(t))
    return y

listx = []
listy = []

#gerando os dados do dataset aleatóriamente 
for i in range(1000): 
    auxx = rd.randint(0, 1000)
    listx.append(auxx)
    auxy = formula(auxx, a)
    listy.append(auxy)

data = {'x': listx, 'y': listy}

#criação do dataset
dataset = pd.DataFrame(data, columns = ['x', 'y']) 

#Definindo a coluna id
dataset.index.name = 'id'

#guardando em um arquivo
dataset.to_csv('dataframe.csv')

#Criação da rede neural
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

dfX = pd.read_csv('dataframe.csv')['x'].copy()

dfY = pd.read_csv('dataframe.csv')['y'].copy() 


X_train, X_test, y_train, y_test = train_test_split(dfX, dfY, test_size=0.25, random_state=0)

X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

regr = MLPRegressor(random_state=1, max_iter=500, solver="lbfgs").fit(X_train, y_train)

y_prev = regr.predict(X_test)

score = regr.score(X_test, y_test)
print("\n\nO score foi: " + str(score))

#função de ativação de saída
print("A função de ativação: " + str(regr.out_activation_))

from sklearn.metrics import mean_absolute_error

erro = mean_absolute_error(y_test, y_prev)

print("O erro foi: " + str(erro))
