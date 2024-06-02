import matplotlib.pyplot as plt
import numpy as np

countries = ['США', 'Німеччина', 'Франція', 'Італія', 'СРСР']
years = [1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000]
values = [
    [43, 56, 69, 76.5, 93.5, 105, 128.5, 146, 157.5, 175],
    [16, 19, 20, 21.5, 23, 29, 37, 40.5, 46.5, 52.5],
    [21.5, 22, 22.5, 23, 23.5, 29.5, 47, 53, 65, 76.5],
    [13.5, 14.5, 16, 17, 18.5, 30.5, 42, 44.5, 49, 56],
    [37, 50.5, 58.8, 63, 75, 81.5, 87.5, 98, 120, 100]
]

fig, ax = plt.subplots()
bar_width = 0.1
index = np.arange(len(years))
for i, country in enumerate(countries):
    ax.bar(index + i * bar_width, values[i], bar_width, label=country)

ax.set_xlabel('Роки')
ax.set_ylabel('Значення')
ax.set_title('2D стовпчикова діаграма')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(years, rotation=90)
ax.legend()
plt.tight_layout()
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_pos = np.arange(len(countries))
y_pos = np.arange(len(years))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)

x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = []

for x, y in zip(x_pos, y_pos):
    country_idx = int(x)
    year_idx = int(y)
    z_pos.append(values[country_idx][year_idx])

ax.bar3d(x_pos, y_pos, np.zeros(len(z_pos)), 0.3, 0.3, z_pos, shade=True)

ax.set_xlabel('Країни')
ax.set_ylabel('Роки')
ax.set_zlabel('Значення')
ax.set_xticks(np.arange(len(countries)))
ax.set_yticks(np.arange(len(years)))
ax.set_xticklabels(countries)
ax.set_yticklabels(years)
ax.set_title('3D стовпчикова діаграма')
plt.show()