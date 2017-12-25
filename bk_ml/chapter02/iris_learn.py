# -*- coding:utf-8 -*-
# encoding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('../data/iris.csv', header=None)
print(df)

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# 只要萼片长度和花瓣长度
x = df.iloc[0:100, [0, 2]].values
# scatter：散点图
plt.scatter(x[0:50, 0], x[0:50, 1], color='red', marker='o', label='setosa')
plt.scatter(x[50:100, 0], x[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')

plt.show()

from perceptron import Perceptron
ppn = Perceptron(eta=0.1)
ppn.fit(x, y)

plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
plt.xlabel(u'Epochs')
plt.ylabel(u'Number of misclassifications')
plt.show()



