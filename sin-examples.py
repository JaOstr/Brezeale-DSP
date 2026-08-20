import numpy as np
import matplotlib.pyplot as plt

A0 = 2
A1 = 3
phi = np.pi/6
T = 4

t = np.linspace(0, 1, 1000)
x1 = A0 + A1 * np.cos(T * 2*np.pi*t + phi)

plt.plot(t, x1)
plt.grid()
plt.xticks([0, 1/4, 0.5, 3/4, 1])
plt.show()

