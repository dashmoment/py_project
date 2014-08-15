import numpy as np
import matplotlib.pyplot as plt
import mlpy
np.random.seed(0)
mean, cov, n = [1, 5], [[1,1],[1,2]], 200
d = np.random.multivariate_normal(mean, cov, n)
x, y = d[:, 0].reshape(-1, 1), d[:, 1]
x.shape

#ols = mlpy.OLS()#Ordinary (Linear) Least Squares Regression (OLS)
ols = mlpy.Ridge(1)#Ridge regression

ols.learn(x, y)
xx = np.arange(np.min(x), np.max(x), 0.01).reshape(-1, 1)
yy = ols.pred(xx)
fig = plt.figure(1) # plot
plot = plt.plot(x, y, 'o', xx, yy, '--k')
plt.show()
