import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.4, 0.6, 1000)

# mn is the minimum value read from the graph
# mx is the maximum value read from the graph
# T is the period read from the graph
# t0 is the cosine starting point read from the graph
mn = -6
mx = 2
T = 0.1
t0 = 0.425

A1 = (mx - mn) / 2     # 4
A0 = mx - A1           # -2
omega = 2 * np.pi / T  # 20pi
phi = omega * t0       # 8.5pi

x = A0 + A1 * np.cos(omega * t - phi)

plt.plot(t, x)
plt.grid()
plt.tight_layout()
plt.show()

