import numpy as py
from scipy.linalg import solve

A = [[1, 1, 1], [0, 1, -3], [2, 1, 5]]
b = [[2], [1], [0]]

x = solve(A,b)
print(x)
