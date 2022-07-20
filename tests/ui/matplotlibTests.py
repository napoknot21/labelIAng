import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame as dt
"""

fig, ax1 = plt.subplots(1, 1)
# make a little extra space between the subplots
fig.subplots_adjust(hspace=0.5)

dt = 0.01
t = np.arange(0, 30, dt)

# Fixing random state for reproducibility
np.random.seed(19680801)


nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2
r = np.exp(-t / 0.05)
 
cnse1 = np.convolve(nse1, r, mode='same') * dt   # colored noise 1
cnse2 = np.convolve(nse2, r, mode='same') * dt   # colored noise 2

# two signals with a coherent part and a random part
s1 = 0.01 * np.sin(2 * np.pi * t) + cnse1
s2 = 0.01 * np.sin(2 * np.pi * t) + cnse2

ax1.plot(t, s1, t, s2)
ax1.set_xlim(0, 5)
ax1.set_xlabel('time')
ax1.set_ylabel('s1 and s2')
ax1.grid(True)
"""

data = pd.read_csv("tests/VehicleData.csv")

data

values0 =  [1.2, 2.2, 3.2, 4.2, 5.2, 5.4, 6.2, 6.4, 6.0, 10.0]

values1 = np.array([1.2, 2.2, 3.2, 4.2, 5.2, 5.4, 6.2, 6.4, 6.0, 10.0])
values2  = np.array([5.3, 6.3, 7.3, 8.3, 9.0, 1.0, 4.8, 5.6, 2.1, 7.6])





print(values1.ndim)

#plt.plot(timer, values1)
#plt.plot(timer, values2)

#plt.show()
