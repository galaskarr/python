# Projeto "Hello World!!" de Machine Learning

#Load libraries

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#Load dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv('C:\\Users\\fsantos\\Documents\\Python\\dataSet\\iris.csv', names=names)

#Shape - Dimensoes do conjunto de dados
print(dataset.shape)

#Head - Dar uma olhada nos dados (to eyeball)
print(dataset.head(20))

#Descriptions - Resumo dos dados
print(dataset.describe())

#Class distribution - Numero de instancias(linhas) que pertencem a cada classe
print(dataset.groupby('class').size())

#Visualizacao dos dados
#box and whisker plots

#Graficos de dados univaridados
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

#Histograms
dataset.hist()
plt.show()

#Graficos de dados multivariados

#scatter plot matrix
scatter_matrix(dataset)
plt.show()


#Avaliando alguns algotitmos
# Criação de alguns modelos de dados e estimar sua acuracia/precisao a partir de novos dados


#Separando dados de validacao

array = dataset.values

X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size = validation_size, random_state = seed)