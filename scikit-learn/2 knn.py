import pandas as pd
import numpy as np
from sklearn import neighbors

train = pd.read_csv("spambase.train", header=None)
Xtrain = train.values[:,:-1]
ytrain = train.values[:,-1:]
#ytrain.shape
#ytrain.ravel()
test = pd.read_csv("spambase.test", header=None)
Xtest = test.values[:,:-1]
ytest = test.values[:,-1:]

def accuracy(y1, y2):
    count = 0
    for i in range(len(y1)):
        if (y1[i] >= 0.5) and (y2[i] >= 0.5) or (y1[i] < 0.5) and (y2[i] < 0.5):
            count += 1
    return 100 * count / len(y1)

n_neighbors = 15
clf = neighbors.KNeighborsClassifier(n_neighbors, weights='uniform')
clf.fit(Xtrain, ytrain.ravel())
Z = clf.predict(Xtest)
#print(sum(abs(Z-ytest.ravel()))/len(Z))
print(accuracy(Z, ytest.ravel())
