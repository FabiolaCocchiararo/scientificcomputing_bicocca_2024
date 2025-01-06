'''
Q1: Fun with arrays

A. Create the array:

[[1,  6, 11],
 [2,  7, 12],
 [3,  8, 13],
 [4,  9, 14],
 [5, 10, 15]]
without explicitly typing it in.

Now create a new array containing only its 2nd and 4th rows.

B. Create a 2d array with 1 on the border and 0 on the inside, e.g., like:

1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
Do this using array slice notation to let it work for an arbitrary-sized array
'''

import numpy as np

#A. 
a = np.arange(1,16).reshape(3,5).T
print(a)
b = np.array([a[1,:], a[3,:]])
print(b)

#B.
n_rows = 5
n_cols = 3
array = np.ones((n_rows, n_cols), dtype=int)
array[1:-1, 1:-1] = 0
print(array)
