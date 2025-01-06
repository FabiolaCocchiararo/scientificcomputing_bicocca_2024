'''
Q4: Climate

Download the data file of global surface air temperature averages from here: https://raw.githubusercontent.com/sbu-python-summer/python-tutorial/master/day-4/nasa-giss.txt This data comes from: https://data.giss.nasa.gov/gistemp/graphs/

(Don't ask, of course you can download data straight from python! Packages requests and urllib can both do the job)

There are 3 columns here: the year, the temperature change, and a smoothed representation of the temperature change.

Read in this data using np.loadtxt().
Plot as a line the smoothed representation of the temperature changes.
Plot as points the temperature change (no smoothing). Color the points blue if they are < 0 and color them red if they are >= 0
You might find the numpy where() function useful.

'''

import numpy as np
import matplotlib.pyplot as plt

year         = np.loadtxt("nasa_data.txt", usecols=(0))
no_smoothing = np.loadtxt("nasa_data.txt", usecols=(1))
lowess       = np.loadtxt("nasa_data.txt", usecols=(2))

plt.plot(year, lowess, label='Lowess', color='tab:green')
colors = np.where(no_smoothing >= 0, 'tab:red', 'tab:blue')
plt.scatter(year, no_smoothing, c=colors, label='No Smoothing')

plt.axhline(0, color='tab:grey', linestyle='--')  
plt.title('Global surface air temperature averages')
plt.xlabel('Year')
plt.ylabel('Temperature Change (°C)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()