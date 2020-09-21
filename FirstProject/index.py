import pandas as pd
import numpy as np
import random

dfOrigem = pd.read_csv("dataCSV/breast-cancer.csv", index_col=0)

#Definindo os nomes da coluna
dfOrigem.columns = ['Clump-Thickness', 'Cell-Size', 'Cell-Shape', 'Marginal-Adhesion', 'Epithelial-Cell-Size', 'Bare-Nuclei', 'Bland-Chromatin', 'Normal-Nucleoli', 'Mitoses', 'Class']

#Definindo a coluna id
dfOrigem.index.name = 'id'

#ordenando em ordem crescente de ids
dfOrigem.sort_index()            

##### TRATAMENTO DE VALORES NULOS
'''
Os valores nulos no problema são indentificados como '?'
Então para ficar mais fácil trocaremos os valores pelo valor np.nan
'''
dfOrigem = dfOrigem.replace('?', np.nan)

#checando aonde estão os valores nulos. Resultado: 16 valores no Bare-Nucleoli
#print('Quantidade de valores nulos do dataset original atuais:')
print('\n\n')
print(dfOrigem.isnull().sum())
print('\n\n')

#substituindo os valores nulos por valores randomicos
dfOrigem = dfOrigem.fillna(random.randint(1, 10))

##### PREPARANDO O DATASET PARA A PREDIÇÃO
#Copiando as respostas e substituindo os resultados por 0 e 1
dfClasse = dfOrigem['Class'].copy()
dfClasse = dfClasse.replace(2, 0).replace(4, 1)

dfOrigem = dfOrigem.drop(columns='Class')

##### CLASSIFICADOR

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

#dividindo dados em teste e treinamento 
# Usou-se 25%(test_size = 0.25) como quantidade de atributos para teste e o restante para treinamento
X_train, X_test, Y_train, Y_test = train_test_split(dfOrigem, dfClasse, test_size=0.25, random_state=0)

#atribuindo a função a uma variável para ser utilizada
classificador = MLPClassifier(random_state=0, max_iter=300)

#treinando o modelo com os valores separados para treinamento
classificador.fit(X_train, Y_train)

#realizando previsão usando o classificador perceptron multicamadas
classificador.predict_proba(X_test)

#precisão média nos dados de teste
classificador.score(X_test, Y_test)

#função de ativação de saída
print('\n\nA função de ativação de saída foi: ' + str(classificador.out_activation_))

### FUNÇÃO PARA MEDIR A ACURÁCIA DO CLASSIFICADOR

from sklearn.metrics import confusion_matrix

y_pred = classificador.predict(X_test)

def accuracy(confusion_matrix):
   diagonal_sum = confusion_matrix.trace()
   sum_of_all_elements = confusion_matrix.sum()
   return diagonal_sum / sum_of_all_elements

cm = confusion_matrix(y_pred, Y_test)
ac = accuracy(cm)

#Printing the accuracy
print("Accuracy of MLPClassifier : " + str(ac))

#PLOTANDO OS DADOS 
from sklearn.svm import SVC

clf = SVC(random_state=0)
clf.fit(X_train, Y_train)

from sklearn.metrics import mean_absolute_error

erro = mean_absolute_error(Y_test, y_pred)

print("O erro foi de: " + str(erro) + "\n\n")

