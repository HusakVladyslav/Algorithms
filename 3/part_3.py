import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-7, 7, 10)
y = np.linspace(-7, 7, 10)
z = np.linspace(-7, 7, 3)

X, Y, Z = np.meshgrid(x, y, z)

Fx = X**2 / (X**3 + Y**3 + Z**3)
Fy = Y**2 / (X**3 + Y**3 + Z**3)
Fz = Z**2 / (X**3 + Y**3 + Z**3)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

ax.quiver(X, Y, Z, Fx, Fy, Fz, length=1, normalize=True, color='black')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Векторне поле: F = (x^2 / (x^3 + y^3 + z^3), y^2 / (x^3 + y^3 + z^3), z^2 / (x^3 + y^3 + z^3))')

plt.show()
