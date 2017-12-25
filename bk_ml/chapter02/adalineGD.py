# -*- coding: utf-8 -*-

#   file-name | adalineGD
#      author | qzhd
#        date | 2017/12/25
# description |
import numpy as np
class AdalineGD(object):

    def __init__(self, eta=0.01, n_iter=50):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, x, y):
        self.w_ = np.zeros(1 + x.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            output = self.net_input(x)
            errors = y - output
            #
            self.w_[1:] += self.eta * x.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()

            cost = (errors ** 2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, x):
        return np.dot(x, self.w_[1:]) + self.w_[0]

    def activation(self, x):
        return self.net_input(x)

    def predict(self, x):
        return np.where(self.activation(x) >= 0.0, 1, -1)