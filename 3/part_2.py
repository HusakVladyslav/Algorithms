import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def u(x):
    return x**3

def v(y):
    return -y**3

xx, yy = np.meshgrid(np.linspace(-8, 8, 20), np.linspace(-8, 8, 20))
u_val = u(xx)
v_val = v(yy)

plt.quiver(xx, yy, u_val, v_val)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.streamplot(xx, yy, u_val, v_val)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
