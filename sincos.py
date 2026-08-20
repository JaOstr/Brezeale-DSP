import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 2*np.pi, 1000)

plt.plot(t, np.sin(t))
plt.plot(t, np.cos(t))
plt.grid()
plt.legend(['sine', 'cosine'])
plt.xticks([0,   np.pi/2,            np.pi,    3*np.pi/2,           2*np.pi],
           ["0", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])
plt.show()

