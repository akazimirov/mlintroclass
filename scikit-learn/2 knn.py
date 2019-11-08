import pandas as pd
import numpy as np
from sklearn import neighbors

train = pd.read_csv("spambase.train")
Xtrain = train.values[:,:-1]
ytrain = train.values[:,-1:]
#ytrain.shape
#ytrain.ravel()
test = pd.read_csv("spambase.test")
Xtest = test.values[:,:-1]
ytest = test.values[:,-1:]

def accuracy(y1, y2):
    ...
    return ...

n_neighbors = 15
clf = neighbors.KNeighborsClassifier(n_neighbors, weights='uniform')
clf.fit(Xtrain, ytrain.ravel())
Z = clf.predict(Xtest)
print(sum(abs(Z-ytest.ravel()))/len(Z))
#print(accuracy(Z, ytest.ravel())
