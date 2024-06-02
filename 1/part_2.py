import numpy as np
import matplotlib.pyplot as plt

def z(x, y):
    return 5 * y * (np.cos(x - 5)**2) - 5 * y**3 * np.exp(y + 1)

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)
z = z(x, y)

fig = plt.figure(label='Графік поверхні')
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Поверхня z = 5 * y * (cos(x - 5)^2) - 5 * y^3 * e^(y + 1)')
plt.show()