'''
Lesson 7 ex Q2: Consistent plotting
'''

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def plot_decorator(function):
    def wrapper(*args, **kwargs):
        fontsize = 14
        matplotlib.rcParams['font.size'] = fontsize
        matplotlib.rcParams['axes.labelsize'] = fontsize
        matplotlib.rcParams['xtick.labelsize'] = fontsize
        matplotlib.rcParams['ytick.labelsize'] = fontsize
        matplotlib.rcParams['legend.fontsize'] = fontsize
        matplotlib.rcParams['legend.fancybox'] = False
        matplotlib.rcParams["legend.frameon"] = False
        matplotlib.rcParams["savefig.facecolor"] = '#ffffff'
        matplotlib.rcParams["axes.titlesize"] = fontsize
        
        plt.figure(figsize=(7,5))
        output = function(*args, **kwargs)
        #plt.savefig('plot.pdf')
        plt.show()

        return output  
    return wrapper

@plot_decorator
def plot(x, y):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.xlabel('sin(x)')

x = np.linspace(0, 10)
y = np.sin(x)
plot(x, y) 
