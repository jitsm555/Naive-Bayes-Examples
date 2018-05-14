import numpy as np
from sklearn.naive_bayes import GaussianNB
# To calculate the accuracy score of the model
from sklearn.metrics import accuracy_score


Weather = np.array([[0], [1], [2], [0], [0], [1], [2], [2], [0], [2], [0], [1], [1], [2]])
Play = np.array([0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0])

# Weather = np.array([[1], [2], [3], [4]])
# Play = np.array([0, 1, 3, 4])

clf = GaussianNB()
clf.fit(Weather, Play)
print(clf.predict([[1]]))
print(clf.score(Weather, Play))
print(accuracy_score(Weather, Play))