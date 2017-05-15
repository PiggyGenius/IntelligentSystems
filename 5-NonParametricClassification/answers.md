### Question 1

K = 20
M = 100
D = 6
N = 20 ??????
Q = N^D = a lot ?

We don't have M >> Q^D, we must adapt the size of the cell to the data.

Cd = (pi^(D / 2)) / gamma((D / 2) + 1)
Cd = (pi^(6 / 2)) / gamma((6 / 2) + 1)
Cd = 1.29

V = Cd ||X - Xs||^D

P(Wk | X) = P(X | Wk) * P(Wk) / P(X)

P(X) = S / (M * V)
P(X | Wk) = Sk / (Mk * V) (Sk = number of points of class k in cluster of S points)
P(Wk) = Mk / M


### Question 2

K = 2
M = 100
D = 3
N = a lot ?
Q = N^D = a lot ?

We don't have M >> Q^D, we must adapt the size of the cell to the data.

S = some kernel function (lets say gaussian)
V = w^D (w size of the thing)

P(Wk | X) = P(X | Wk) * P(Wk) / P(X)

P(X) = S / (M * V)
P(X | Wk) = Sk / (Mk * V) (Sk = number of points of class k in cluster of S points)
P(Wk) = Mk / M

### Question 3

K = 100
M = 1000
D = 1
N = 10
Q = N^D = a lot ?

We have M >> Q^D. We use a ratio of histograms.
