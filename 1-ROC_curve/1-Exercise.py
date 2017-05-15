#!/usr/bin/python3.6
# -*-coding:Utf-8 -*
import numpy as np
import matplotlib.pyplot as plt

# Our set consists of 40 samples of one feature x in {1,2,3,4}. Ten samples for each possible value.
class_range = [2, 4, 6, 8]
values = [] ; classes = []
for i in range(1, 5):
    values += [i for j in range(0, 10)]
    classes += [1 for j in range(0, class_range[i-1])]
    classes += [0 for j in range(0, 10 - class_range[i-1])]
data = np.array(tuple(zip(values, classes)))

# We setup our histogram data
h_1 = [] ; h_2 = []
for i in range(1, 5):
    h_1.append(len(data[np.all(np.equal(data, (i,1)), axis = 1)]))
    h_2.append(len(data[np.all(np.equal(data, (i,0)), axis = 1)]))

# We define g(x) = h_1(x) / h(x) and d(x) = 1 if g(x) >= 0.5 and 0 otherwise
def g(x):
    x = x-1
    return h_1[x] / (h_1[x] + h_2[x])
def d(x):
    return 1 if g(x) > 0.5 else 0
def d_bias(x, bias):
    return 1 if g(x) + bias >= 0 else 0

# We construct the bias array
bias = []
for i in range(1, 5):
    bias.append(-g(i))

# Now we get the TPR and FPR rates for each value of the bias
precision, TPR, FPR = [], [], []
P = np.count_nonzero(data[:, 1]) 
N = len(data) - P
for b in bias:
    TP = FP = 0
    for d_x in data:
        if d_bias(d_x[0], b) == d_x[1] and d_bias(d_x[0], b) == 1:
            TP += 1
        elif d_bias(d_x[0], b) != d_x[1] and d_bias(d_x[0], b) == 1:
            FP += 1
    precision.append(TP / (TP + FP))
    TPR.append(TP / P)
    FPR.append(FP / N)

# We plot the ROC curve
plt.plot(FPR,TPR, label = 'Histogram classifier')
plt.plot([0, 1],[0, 1], linestyle = '--', color = (0.6, 0.6, 0.6), label = 'Random guessing')
plt.plot([0, 0, 1], [0, 1, 1], linestyle = ':', color = 'black', label = 'Perfect performance')
plt.title('ROC curve')
plt.legend(loc = "lower right")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.show()

####################################################################################################
# ************************************************************************************************ #
# *                                         ANSWERS                                                #
# ************************************************************************************************ #
# 1) g(x) = h_1(x) / (h_1(x) + h_2(x)) ; d(x) = 1 if g(x) > 0.5 and 0 otherwise                    #
# 2) g(x) + B_x = 0 ==> B_x = -g(x) ==> B_x = (-0.2, -0.4, -0.6, -0.8)
#                                                                                                  #
####################################################################################################

print('1) g(x) = h_1(x) / (h_1(x) + h_2(x)) ; d(x) = 1 if g(x) > 0.5 and 0 otherwise.')
print('2) g(x) + B_x = 0 ==> B_x = -g(x) ==> B_x = {}.'.format(bias))
print('3-5)Bias = {} \n\t\tTPR = {} ; FPR = {} ; Precision = {} ; Recall = {}'.format(bias[0],TPR[0],FPR[0], precision[0], TPR[0]))
bias.pop(0)
for b, i in zip(bias,range(1,4)):
    print('\tBias = {} \n\t\tTPR = {} ; FPR = {} ; Precision = {} ; Recall = {}'.format(b,TPR[i],FPR[i], precision[i], TPR[i]))
