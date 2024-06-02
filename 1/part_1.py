import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return 7 * np.sin(x * np.pi) - np.cos(3 * np.pi * x) * np.sin(np.pi * x)

def z1(x):
  return (np.sqrt(1 + np.abs(x))) / (2 + np.abs(x))

def z2(x):
  return (1 + x) / (2 + np.power(np.cos(x), 3))

x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)

y = f(x)

plt.plot(x, y, label="7 * sin(pi * x) - cos(3 * pi * x) * sin(pi * x)")

first = np.linspace(-5 * np.pi, 0, 1000)

z1 = z1(first)

plt.plot(first, z1, label="(sqrt(1 + |x|)) / (2 + |x|), x <= 0")

second = np.linspace(0, 5 * np.pi, 1000)

z2 = z2(second)

plt.plot(second, z2, label="(1 + x) / (2 + (cos(x))^3), x > 0")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.text(-17, 20, "y = 7 * sin(pi * x) - cos(3 * pi * x) * sin(pi * x)", fontsize=10)
plt.text(-6, 21, "{ (sqrt(1 + |x|)) / (2 + |x|), x <= 0", fontsize=10)
plt.text(-6.8, 20, "z = { ")
plt.text(-6, 19, "{ (1 + x) / (2 + (cos(x))^3), x > 0", fontsize=10)
plt.show()
