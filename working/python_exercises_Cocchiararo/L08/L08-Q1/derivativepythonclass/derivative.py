'''
Test create a python package 
'''

import numpy as np

def derivative(x, func):
    der = []
    for i in range(len(func)-1):
        diff   = func[i+1]-f[i]
        deltax = x[i+1]-x[i]
        der.append(diff/deltax)
    return der
