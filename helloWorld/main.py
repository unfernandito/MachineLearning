import sys
from sklearn import tree

data = [[29, 0], [27, 0], [22, 1], [18, 1]]
labels = ["macho", "macho", "hembra", "hembra"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data, labels)

print clf.predict([[sys.argv[1], sys.argv[2]]])
