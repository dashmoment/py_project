import numpy as np
import matplotlib.pyplot as plt
import mlpy

extx_path = 'C:/Python27/ex2x.dat'
exty_path = 'C:/Python27/ex2y.dat'

fx = open(extx_path)
fy = open(exty_path)

xx = []
yy = []

for each in fx:
    xx.append(float(each))

for each in fy:
    yy.append(float(each))

plt.figure()  
plt.plot(xx,yy,'*')
plt.xlabel('Height in meters')
plt.ylabel('Age in years')

new_x = []

for each in xx[0:5]:
    a=[]
    a.append(1)
    a.append(each)
    new_x.append(a)

for each in xx[5:]:
    a=[]
    a.append(1)
    a.append(each)
    new_x.append(a)


beta ,rank =  mlpy.ols_base(new_x , yy ,0.05)

test_x = [[1,3.5] ,[1,7]]
test_xx = []
for i in test_x:
    test_xx.append(i)

test_y = []
for each in test_x:
    temp = beta[0]*each[0]+beta[1]*each[1]
    test_y.append(temp)
    print(test_y)

plt.plot(test_xx,test_y,'o')

plot_x=np.arange(np.min(xx),np.max(xx),0.1)
plot_y = [beta[0]+beta[1]*i for i in plot_x]
plt.plot(plot_x,plot_y,'--k')

plt.show()
