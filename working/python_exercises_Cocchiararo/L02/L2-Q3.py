'''
Q3: Are you faster than numpy? No

Numpy of course has a standard deviation function, np.std(), 
but here we'll write our own that works on a 1-d array (vector). 
The standard deviation is a measure of the "width" of the 
distribution of numbers in the vector.

Write a function to calculate the standard deviation for an input array, a:

-First compute the average of the elements in a to define 
-Next compute the sum over the squares of 
-Then divide the sum by the number of elements in the array
-Finally take the square root (you can use np.sqrt())

Test your function on a random array, and compare to the built-in np.std(). Check the runtime as well.

'''

import numpy as np
import random
import time 

a            = np.linspace(0,1000,int(1.e5))

t0           = time.time()
a_mean       = np.mean(a)
squared_diff = np.sum((a-a_mean)**2)
squared_diff = squared_diff/len(a)
std          = np.sqrt(squared_diff)
t1           = time.time()
print('time to compute the std using my function:', t1-t0)

t2    = time.time()
a_std = np.std(a)
t3    = time.time()
print('time to compute the std using python function:', t3-t2)