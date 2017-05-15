#!/usr/bin/python3.6
# -*-coding:Utf-8 -*
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = make_blobs(n_samples = 200, n_features = 2, centers = 20, center_box = (0, 20), shuffle = True, random_state = 0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)

knn = KNeighborsClassifier(n_neighbors = 5, p = 2, metric = 'minkowski')
knn.fit(X_train, y_train)

print("Accuracy: {}".format(accuracy_score(knn.predict(X_test), y_test)))
