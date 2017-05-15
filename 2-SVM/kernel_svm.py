#!/usr/bin/python3.6
# -*-coding:Utf-8 -*
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import rbf_kernel
from matplotlib.colors import ListedColormap

# We create our learning discriminant function
support_vectors = []
def g(X, Y, A):
    for  x, y, a in zip(X, Y, A):
        if a != 0:
            support_vectors.append((x, y, a))

def predict(X):
    s = 0
    for v in support_vectors:
        s += v[2] * v[1] * rbf_kernel(X, v[0].reshape(1, -1), 1/2)
    return s

# We create our data samples
X_1 = [1, 1, 2, 3, 3, 1, 3, 5, 5, 5]
X_2 = [1, 3, 2, 1, 3, 5, 5 ,1, 3, 5]
X = np.array(tuple(zip(X_1, X_2)))
Y = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]
A = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0]

# We train our discriminant function
p_X = np.array([1, 2]).reshape(1, -1)
g(X, Y, A)

# We plot the decision region
markers = ('o', 'o')
colors = ('red', 'blue')
cmap = ListedColormap(colors[:2])
x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.02), np.arange(x2_min, x2_max, 0.02))
Z = predict(np.array([xx1.ravel(), xx2.ravel()]).T)
Z = Z.reshape(xx1.shape)
plt.contourf(xx1, xx2, Z, alpha = 0.4, cmap = cmap)
plt.xlim(xx1.min(), xx1.max())
plt.ylim(xx2.min(), xx2.max())

for idx, cl in enumerate(np.unique(Y)):
    plt.scatter(x = X[Y == cl, 0], y = X[Y == cl, 1], alpha = 0.8, c = cmap(idx), marker = markers[idx], label = cl)
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc = 'upper right')
plt.title('SVM decision region with RBF kernel')
plt.show()

# We check if our data is seperated by our discriminant function
correct = 0
for x, y in zip(X, Y):
    if predict(x.reshape(1, -1)) > 0 and y == 1:
        correct += 1
    elif predict(x.reshape(1, -1)) < 0 and y == -1:
        correct += 1


####################################################################################################
# ************************************************************************************************ #
# *                                         ANSWERS                                                #
# ************************************************************************************************ #
#                                                                                                  #
####################################################################################################

print('1) g(X) = exp(-1/2 * ||X-X_2||^2) - exp(-1/2 * ||X-X_7||^2) - exp(-1/2 * ||X-X_9||^2)')
print('2) By looking at the decision region we can see that the data is seperable with this discriminant function. We can also try to predict our training data to check if we managed to seperate the data or if we need a slack variable.')
print('Percentage of accurate predictions on our training data: {}%.'.format(correct * 100 / len(X)))
