import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x = np.linspace(0, 8, 50)
y = np.linspace(0, 8, 50)
X, Y = np.meshgrid(x, y)

scalar_field = X * (Y**2) - np.sqrt((X**3) * Y)

gradient_x, gradient_y = np.gradient(scalar_field)

fig, ax = plt.subplots(figsize=(10, 8))
cs = ax.contourf(X, Y, scalar_field, cmap='viridis')
fig.colorbar(cs)
ax.set_title('Скалярне поле: x * (y^2) - sqrt((y^3) * Y)')
ax.set_xlabel('x')
ax.set_ylabel('y')

fig, ax = plt.subplots(figsize=(10, 8))
q = ax.quiver(X, Y, gradient_x, gradient_y, color='b')
ax.set_title('Градієнт скалярного поля')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()