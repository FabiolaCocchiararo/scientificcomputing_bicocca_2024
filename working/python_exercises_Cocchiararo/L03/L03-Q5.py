'''
Q5: Subplots

matplotlib has a number of ways to create multiple axes in a figure 
-- look at plt.subplots() 
(http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot)

Create an x array using NumPy with a number of points, 
spanning from [0,2pi].

Create 3 axes vertically, and do the following:

-Define a new numpy array f initialized to a function of your 
choice.
-Plot f in the top axes
-Compute a numerical derivative of f,
f'=(f_(i+1)-fi)/deltax
 
and plot this in the middle axes

-Do this again, this time on f' to compute the second derivative 
and plot that in the bottom axes

'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def derivative(x, func):
    der = []
    for i in range(len(func)-1):
        diff   = func[i+1]-f[i]
        deltax = x[i+1]-x[i]
        der.append(diff/deltax)
    return der 
xPoints = np.linspace(0,2*np.pi, endpoint=True)

fig = plt.figure()
gs  = GridSpec(3, 1, figure=fig)

ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[1,0])
ax3 = fig.add_subplot(gs[2,0])

f      = np.sin(xPoints)
f_der  = derivative(xPoints, f)
f_der2 = derivative(xPoints[:-1], f_der)

ax1.plot(xPoints,f, label=r'f(x)')
ax2.plot(xPoints[:-1],f_der, color='tab:orange',label=r"$f'(x)$")
ax3.plot(xPoints[:-2],f_der2, color='tab:green',label=r"$f''(x)$")

ax1.legend()
ax2.legend()
ax3.legend()

ax1.set_ylabel('y')
ax2.set_ylabel('y')
ax3.set_ylabel('y')

ax3.set_xlabel('x')

#plt.grid(alpha=0.3)
plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
