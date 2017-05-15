#!/usr/bin/python3
# -*-coding:Utf-8 -*
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sigmoid(net_input):
    return 1.0 / (1.0 + np.exp(np.negative(net_input)))

def net_input(X, W_1, W_2, B_1, B_2):
    activation_unit = []
    for i in range(0,3):
        activation_unit.append(np.dot(W_1[i], X) + B_1[i])
    activation_unit.append(np.dot(W_2, sigmoid(activation_unit)) + B_2)
    return activation_unit

def output_error(activation, y):
    return activation * (1 - activation) * (activation - y)

def error(activation, W, output):
    return activation * (1 - activation) * np.dot(W, output)

def update_weight(activation_units, error_output, error_outputs, X):
    W_2_update = []
    W_1_update = []
    for i in range(0, 3):
        W_1_update.append([X[0] * error_outputs[i], X[1] * error_outputs[i]])
    for i in range(0, 3):
        W_2_update.append(activation_units[i] * error_output)
    return np.array(W_1_update), np.array(W_2_update)


B_1 = np.array([-1, 0, 1])
B_2 = 1
W_1 = np.array([[1, 0], [-1, 0], [0, 1]])
W_2 = np.array([1, -1, 0])
X = np.array([[1, 0], [1, 1], [0, 1], [0, 0]])
y = np.array([1, 0, 1, 0])
net_inputs = net_input(X[0], W_1, W_2, B_1, B_2)
activation_units = [sigmoid(net_inputs[0]), sigmoid(net_inputs[1]), sigmoid(net_inputs[2]), sigmoid(net_inputs[3])]
error_output = output_error(activation_units[3], y[0])
error_outputs = [error(sigmoid(net_inputs[0]), W_2[0], error_output), error(sigmoid(net_inputs[1]), W_2[1], error_output), error(sigmoid(net_inputs[2]), W_2[2], error_output), ]
W_1_update, W_2_update = update_weight(activation_units, error_output, error_outputs, X[0])

print("a_1^1={}, w_1,1^2={}, d_1^2={}, result={}".format(sigmoid(net_inputs[0]), W_2[0], error_output, error_outputs[0]))

print("1) Output of each unit for the first training sample:")
for i in range(0, 3):
    print("   a_{}^1 = f({}) = {}".format(i + 1, net_inputs[i], activation_units[i]))
print("   a_1^2 = f({}) = {}".format(net_inputs[3], activation_units[3]))

print("2) Error term for each unit by back-propagation for the first training sample:")
print("   d_1^2 = {}".format(error_output))
for i in range(0, 3):
    print("   d_{}^1 = {}".format(i + 1, error_outputs[i]))

print("3) Weight and bias correction  for the first training sample:")
for j in range(0, 3):
    for i in range(0, 2):
        print("   W_{},{}^1 = {}".format(j + 1, i + 1, W_1_update[j][i]))
for i in range(0, 3):
    print("   W_1,{}^2 = {}".format(i + 1, W_2_update[i]))
for i in range(0, 3):
    print("   B_{}^1 = {}".format(i + 1, error_outputs[i]))
print("   B_1^2 = {}".format(error_output))

print("4) Network parameters:")
learning_rate = 0.5
for i in range(0, 4):
    net_inputs = net_input(X[i], W_1, W_2, B_1, B_2)
    activation_units = []
    for j in range(0, 4):
        activation_units.append(sigmoid(net_inputs[j]))
    error_output = output_error(activation_units[3], y[i])
    error_outputs = []
    for j in range(0, 3):
        error_outputs.append(error(activation_units[j], W_2[j], error_output))
    W_1_update, W_2_update = update_weight(activation_units, error_output, error_outputs, X[i])
    W_1 = np.subtract(W_1, np.multiply(learning_rate, W_1_update))
    W_2 = np.subtract(W_2, np.multiply(learning_rate, W_2_update))
    B_1 = np.subtract(B_1, np.multiply(learning_rate, error_outputs))
    B_2 = np.subtract(B_2, np.multiply(learning_rate, error_output))
for j in range(0, 3):
    for i in range(0, 2):
        print("   W_{},{}^1 = {}".format(j + 1, i + 1, W_1[j][i]))
for i in range(0, 3):
    print("   W_1,{}^2 = {}".format(i + 1, W_2[i]))
for i in range(0, 3):
    print("   B_{}^1 = {}".format(i + 1, B_1[i]))
print("   B_1^2 = {}".format(B_2))

print("5) Network parameters without the update for each sample:")
B_1 = np.array([-1, 0, 1])
B_2 = 1
W_1 = np.array([[1, 0], [-1, 0], [0, 1]])
W_2 = np.array([1, -1, 0])
learning_rate = 0.5
W_1_final = np.array([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
W_2_final = np.array([0.0, 0.0, 0.0])
B_1_final = np.array([0.0, 0.0, 0.0])
B_2_final = 0.0
for i in range(0, 4):
    net_inputs = net_input(X[i], W_1, W_2, B_1, B_2)
    activation_units = []
    for j in range(0, 4):
        activation_units.append(sigmoid(net_inputs[j]))
    error_output = output_error(activation_units[3], y[i])
    error_outputs = []
    for j in range(0, 3):
        error_outputs.append(error(activation_units[j], W_2[j], error_output))
    W_1_update, W_2_update = update_weight(activation_units, error_output, error_outputs, X[i])
    W_1_final += W_1_update
    W_2_final += W_2_update
    B_1_final += error_outputs
    B_2_final += error_output

W_1 = np.subtract(W_1, np.multiply(learning_rate, W_1_final / 4))
W_2 = np.subtract(W_2, np.multiply(learning_rate, W_2_final / 4))
B_1 = np.subtract(B_1, np.multiply(learning_rate, B_1_final / 4))
B_2 = np.subtract(B_2, np.multiply(learning_rate, B_2_final / 4))
for j in range(0, 3):
    for i in range(0, 2):
        print("   W_{},{}^1 = {}".format(j + 1, i + 1, W_1[j][i]))
for i in range(0, 3):
    print("   W_1,{}^2 = {}".format(i + 1, W_2[i]))
for i in range(0, 3):
    print("   B_{}^1 = {}".format(i + 1, B_1[i]))
print("   B_1^2 = {}".format(B_2))
