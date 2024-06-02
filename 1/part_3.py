import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)
a = 1
r = (a**3) / (t**2 + a**2)
x = t

plt.figure(figsize=(6, 6))
plt.polar(x, r)
plt.title('Графік у полярних координатах: r = a^3 / (t^2 + a^2)')
plt.grid(True)
plt.show()