import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Функція для оновлення кадрів анімації
def update(frame):
    # Очищення попереднього зображення
    plt.cla()
    
    # Кут обертання
    theta = np.radians(frame)
    
    # Побудова еліпса з врахуванням обертання
    rotated_ellipse = np.dot(rotation_matrix(theta), ellipse.T).T
    
    # Зображення еліпса
    plt.plot(rotated_ellipse[:, 0], rotated_ellipse[:, 1])
    
    # Налаштування вигляду
    plt.axis('equal')
    plt.title('Еліпс, що обертається навколо власного центру')

# Функція для створення матриці обертання
def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

# Параметри еліпса
a = 5  # півосі а
b = 3  # півосі b

# Генерація точок для еліпса
theta = np.linspace(0, 2*np.pi, 100)
ellipse = np.array([a * np.cos(theta), b * np.sin(theta)]).T

# Ініціалізація графіку
fig = plt.figure()
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=50)

# Збереження анімації у форматі GIF
ani.save('rotating_ellipse.gif', writer='pillow')

# Відображення анімації
plt.show()
