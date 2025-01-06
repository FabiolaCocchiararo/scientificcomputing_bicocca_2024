'''
Q5: Planetary orbits
'''

import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def eqs_evolution(t, conditions):
    x,y,vx,vy = conditions 
    #dx_dt  = vx
    #dy_dt  = vy
    r = np.sqrt(x**2+y**2)
    ax = -G*M*x/r**3
    ay = -G*M*y/r**3
    return np.array([vx, vy, ax, ay])

def integration(X0, dt, tmax):
    # with the Radau method it works, with the "RK45" method no. 
    evolution = solve_ivp(eqs_evolution, (0, tmax), X0, method='Radau', t_eval=np.arange(0.0, tmax, dt))
    #ts = np.arange(0.0, tmax,dt)
    return evolution.t, evolution.y

#constants
G = 4.*np.pi**2
M = 1.
a = 1.
e = 0.017 #Earth eccentricity 

#perihelion 
rp = a*(1-e)
vp = np.sqrt(G*M*(1 + e)/rp)

#initial conditions
#xi = rp
#yi = 0.
#vx = 0.
#vy = 0.
X0 = [rp,0,0,vp]

t, X = integration(X0, 0.0001, 2)
plt.plot(X[0], X[1], label='Orbit')
plt.plot(0,0,'.', label='Sun')
plt.grid(alpha = 0.5)
plt.xlabel('X') 
plt.ylabel('Y')
plt.legend()
plt.show()