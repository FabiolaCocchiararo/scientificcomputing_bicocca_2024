'''
Q7: Noisy signal

'''

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import signal
from matplotlib.gridspec import GridSpec

def fdata(x, L):
    A = L/10.0
    return 2*np.sin(2*np.pi*x/L) + x*(L-x)**2/L**3 * np.cos(x) + \
           5*x*(L-x)/L**2 + A/2 + 0.1*A*np.sin(13*np.pi*x/L)

N = 2048
L = 50.0
x = np.linspace(0, L, N, endpoint=False)
orig  = fdata(x, L)
noisy = orig + 0.5*np.random.randn(N)
gaus  = scipy.signal.windows.gaussian(N,std=20)
gaus  = gaus/np.sum(gaus)
conv = signal.convolve(noisy, gaus, mode='same', method='fft')

fig = plt.figure()

plt.plot(x, noisy, label='Noisy signal')
plt.plot(x, orig, label='Data without noise', color='tab:orange')
plt.plot(x, conv, label='Noisy sig + gaus', color='tab:red')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.show()