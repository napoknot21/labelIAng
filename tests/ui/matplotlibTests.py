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

timer_name = data.columns[0]

print(timer_name)

timer = np.array(data[timer_name])

print(timer)

print(timer[1])

print(timer.shape)

data_2 = np.array(data['PP_Model_B__HPP_Z_close'])

data_3 = np.array(data['TSR0__Sign_Width'])

print(data_2)

print(data_2.shape)

print(data_3)

print(data_3.shape)



plt.plot(timer, data_2)
plt.plot(timer, data_3)

plt.show()
