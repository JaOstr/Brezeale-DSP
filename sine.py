import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi)
y = np.sin(t)

plt.grid()
plt.plot(t, y)
plt.show()

