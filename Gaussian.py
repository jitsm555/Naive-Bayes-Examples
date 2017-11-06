# see jupyter notebook to know more about Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()

column_list = ['weather', 'play']
data = pd.read_csv('/Users/jiteshmohite/projects/2017-2018/AI/algo/Naive-Bayes-Examples/wheather.csv',header=None, names= column_list)
print(data)

# gnb = GaussianNB()
#
# y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
# print((iris.target != y_pred).sum())
# print("Number of mislabeled points out of a total %d points : %d"
#       % (iris.data.shape[0],(iris.target != y_pred).sum()))
#
# print(iris.data)
# print("/n/n")
# print(iris.target)
# print(iris.target_names)





