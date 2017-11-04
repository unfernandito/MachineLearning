import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

test_idx = [0,50,100]

# Parseo de data de entrenamiento
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# Data de testeo
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# Ejecucion

print "Resultado esperado: " + str(test_target)

print "Resultado obtenido: " + str(clf.predict(test_data))
