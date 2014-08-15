import numpy as np
import mlpy
import matplotlib.pyplot as plt # required for plotting

iris = np.loadtxt('iris.csv', delimiter=',')
x, y = iris[:, :4], iris[:, 4].astype(np.int)
x.shape
pca = mlpy.PCA()
pca.learn(x)
z = pca.transform(x, k=2)

#plt.set_cmap(plt.cm.Paired)
fig1 = plt.figure(1)
title = plt.title("PCA on iris dataset")
plot = plt.scatter(z[:, 0], z[:, 1], c=y)
labx = plt.xlabel("First component")
laby = plt.ylabel("Second component")


linear_svm = mlpy.LibSvm(svm_type='nu_svc' ,kernel_type='rbf',probability=True) # new linear SVM instance
linear_svm.learn(z, y) # learn from principal components

xmin, xmax = z[:,0].min()-0.1, z[:,0].max()+0.1
ymin, ymax = z[:,1].min()-0.1, z[:,1].max()+0.1


xx, yy = np.meshgrid(np.arange(xmin, xmax, 0.01), np.arange(ymin, ymax, 0.01))
zgrid = np.c_[xx.ravel(), yy.ravel()]
yp = linear_svm.pred(zgrid)
data_p = linear_svm.pred_probability(zgrid)

linear_svm.save_model('svm_for_iris')
svm_iris = mlpy.LibSvm.load_model('svm_for_iris')
yp_iris = svm_iris.pred_probability(zgrid)


#plt.set_cmap(plt.cm.Paired)
fig2 = plt.figure(2)
title = plt.title("SVM (linear kernel) on principal components")
plot1 = plt.pcolormesh(xx, yy, yp.reshape(xx.shape))
plot2 = plt.scatter(z[:, 0], z[:, 1], c=y)
labx = plt.xlabel("First component")
laby = plt.ylabel("Second component")
limx = plt.xlim(xmin, xmax)
limy = plt.ylim(ymin, ymax)
plt.show()
