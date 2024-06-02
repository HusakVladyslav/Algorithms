import numpy as np
import matplotlib.pyplot as plt

a = 2
b = 3
c = 4

x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)
Z = (c / np.sqrt(a**2 + b**2)) * np.sqrt(X**2 / a**2 + Y**2 / b**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Поверхня другого порядку Конус: (x^2/a^2) + (y^2/b^2) - (z^2/c^2) = 0')

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()