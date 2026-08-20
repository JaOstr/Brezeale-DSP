import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 1000)
y = np.sin(2 * np.pi * t)

plt.subplot(2, 1, 1)
plt.plot(t,y)
plt.title("Normal sine")
plt.grid()
plt.xlabel("t")
plt.ylabel("sin(x)")

plt.subplot(2, 1, 2)
plt.plot(t, np.sin(2 * np.pi * 3 * t))
plt.title("Frequency * 3")

plt.show()


