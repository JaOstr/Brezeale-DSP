import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

plt.figure()
y1 = 3 + 2*np.cos(2 * np.pi * 4 * t)
plt.subplot(4, 1, 1)
plt.plot(t, y1)
y2 = 0 + 1*np.cos(2 * np.pi * 5 * t + np.pi/6)
plt.subplot(4, 1, 2)
plt.plot(t, y2)
y3 = -1 +5*np.cos(2 * np.pi * 7 * t - np.pi/4)
plt.subplot(4, 1, 3)
plt.plot(t, y3)

y = y1 + y2 + y3

plt.subplot(4, 1, 4)
plt.plot(t, y)

plt.tight_layout()
plt.grid()
plt.show()

