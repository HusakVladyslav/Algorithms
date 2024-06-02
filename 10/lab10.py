import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE, LocallyLinearEmbedding, Isomap, MDS
from umap import UMAP
from sklearn.preprocessing import StandardScaler

# 1. Завантаження даних
data_path = 'transfusion.data'

# Загружаємо дані
data = pd.read_csv(data_path)

# 2. Попередня обробка даних
X = data.iloc[:, :-1]  # Всі колонки окрім останньої, яка можливо є міткою
y = data.iloc[:, -1]   # Остання колонка, якщо вона є міткою

# Масштабування даних
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Використання методів пониження розмірності
methods1 = {
    'PCA 2D': PCA(n_components=2),
    'PCA 3D': PCA(n_components=3),
    't-SNE 2D': TSNE(n_components=2, random_state=42),
    't-SNE 3D': TSNE(n_components=3, random_state=42),
    'UMAP 2D': UMAP(n_components=2, random_state=42),
    'UMAP 3D': UMAP(n_components=3, random_state=42)
}

methods2 = {
    'LLE 2D': LocallyLinearEmbedding(n_components=2, random_state=42),
    'LLE 3D': LocallyLinearEmbedding(n_components=3, random_state=42),
    'Isomap 2D': Isomap(n_components=2),
    'Isomap 3D': Isomap(n_components=3),
    'MDS 2D': MDS(n_components=2, random_state=42),
    'MDS 3D': MDS(n_components=3, random_state=42)
}

# 4. Візуалізація результатів

fig1, axs1 = plt.subplots(3, 2, figsize=(6, 6))

for i, (method_name, method) in enumerate(methods1.items()):
    ax = axs1[i // 2, i % 2]
    
    X_transformed = method.fit_transform(X_scaled)
    
    if '2D' in method_name:
        sc = ax.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y, cmap='viridis', s=5)
        ax.set_title(f"{method_name}")
    elif '3D' in method_name:
        ax = fig1.add_subplot(3, 2, i + 1, projection='3d')
        sc = ax.scatter(X_transformed[:, 0], X_transformed[:, 1], X_transformed[:, 2], c=y, cmap='viridis', s=5)
        ax.set_title(f"{method_name}")
        ax.set_xticks([])
        ax.set_yticks([])

plt.tight_layout()
plt.show()

fig2, axs2 = plt.subplots(3, 2, figsize=(6, 6))

for i, (method_name, method) in enumerate(methods2.items()):
    ax = axs2[i // 2, i % 2]
    
    X_transformed = method.fit_transform(X_scaled)
    
    if '2D' in method_name:
        sc = ax.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y, cmap='viridis', s=5)
        ax.set_title(f"{method_name}")
    elif '3D' in method_name:
        ax = fig2.add_subplot(3, 2, i + 1, projection='3d')
        sc = ax.scatter(X_transformed[:, 0], X_transformed[:, 1], X_transformed[:, 2], c=y, cmap='viridis', s=5)
        ax.set_title(f"{method_name}")
        ax.set_xticks([])
        ax.set_yticks([])

plt.tight_layout()
plt.show()
