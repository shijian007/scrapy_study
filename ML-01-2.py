import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#读取数据
path = 'ex1data2.txt'
data = pd.read_csv(path,header= None,names = ['Population', 'Bedroom', 'Profit'])
data = (data - data.mean())/data.std()
# data.head()

#对原始数据进行绘图
# data.plot(kind = 'scatter',x = 'Population', y = 'Bedroom', z = 'Profit',figsize = (12,8))
# plt.show()
#
#定义代价函数
def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))

#插入一行全1,为后文公式准备
data.insert(0, 'Ones', 1)

#读取列长度
cols = data.shape[1]
#数据预处理
X = data.iloc[:, 0:cols-1]
y = data.iloc[:, cols-1:cols]

#转化成np矩阵
X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0, 0, 0]))

#计算代价函数
# cost = computeCost(X, y, theta)
# print(cost)

#定义批量梯度下降函数
def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        #微分方程求导后的公式
        error = ( X * theta.T ) -y
        #parameters是theta的长度,每次对一个theta 求导
        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - alpha * np.sum(term)/len(X)

        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta,cost

alpha = 0.01
iters = 1000

g, cost = gradientDescent(X, y, theta, alpha, iters)
print(computeCost(X, y, g))
print(g)

# x = np.linspace(data.Population.min(), data.Population.max(), 100)
# f = g[0,0] + (g[0,1] * x)

#返回一个窗口figure, 和一个tuple型的ax对象，该对象包含所有的子图,可结合ravel()函数列出所有子图
# 函数列出所有子图
fig, ax = plt.subplots(figsize = (12, 8))
ax.plot(range(iters), cost, 'r', label = 'cost')
# ax.scatter(data.Population, data.Profit, label='Traning Data')
ax.legend(loc=1)
ax.set_xlabel('Cost')
ax.set_ylabel('Iters')
ax.set_title('Cost trend')
plt.show()


