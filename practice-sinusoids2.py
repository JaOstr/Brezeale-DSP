import numpy as np
import matplotlib.pyplot as plt

T = 0.02
t = np.linspace(0, T, 1000)

x1 = 3 * np.e ** (np.pi * 2j) * np.e ** (100j * np.pi * t) + \
     3 * np.e ** (np.pi * 2j) * np.e ** (-100j * np.pi * t)
plt.subplot(2, 1, 1)
plt.plot(t, x1)

x2 = 6 * np.cos(100 * np.pi * t)
plt.subplot(2, 1, 2)
plt.plot(t, x2)

plt.grid()
plt.tight_layout()
plt.show()

