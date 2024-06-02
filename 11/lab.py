# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from numpy.linalg import svd

# Load the dataset
data = pd.read_csv('./transfusion.data')

# Extract features (assuming the dataset does not include the header, adjust if necessary)
X = data.values

# Task 1: Using PCA to visualize data in 2D and 3D spaces
# PCA for 2D
pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X)

# PCA for 3D
pca_3d = PCA(n_components=3)
X_pca_3d = pca_3d.fit_transform(X)

# Plotting 2D PCA
plt.figure(figsize=(10, 6))
plt.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c='blue', marker='o')
plt.title('PCA 2D Visualization')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.show()

# Plotting 3D PCA
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_pca_3d[:, 0], X_pca_3d[:, 1], X_pca_3d[:, 2], c='blue', marker='o')
ax.set_title('PCA 3D Visualization')
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
plt.show()

# Task 2: Calculate SVD of the dataset
U, S, VT = svd(X, full_matrices=False)

# Plot the eigenvalues (singular values) in descending order
plt.figure(figsize=(10, 6))
plt.plot(S, 'bo-', markersize=5)
plt.title('Singular Values of the Dataset')
plt.xlabel('Index')
plt.ylabel('Singular Value')

plt.show()

# Task 3: Determine the smallest value of the space size i for which the relation is satisfied
total_variance = np.sum(S)
variance_explained = np.cumsum(S) / total_variance

i = np.argmax(variance_explained >= 0.8) + 1
print(f"Smallest value of space size i for 80% significance level: {i}")

# Task 4: Set λi to zero for which d ≤ i ≤ n and perform reverse transformation
S_reduced = np.copy(S)
S_reduced[i:] = 0
Sigma_reduced = np.diag(S_reduced)

X_approx = np.dot(U, np.dot(Sigma_reduced, VT))

# Compare the obtained data with the original
print("\nOriginal Data (first 5 rows):")
print(X[:5])
print("\nReconstructed Data after SVD reduction (first 5 rows):")
print(X_approx[:5])

# Task 5: Set d = 2 and d = 3 and plot the first d columns of reconstructed data
# d = 2
U_2 = U[:, :2]
Sigma_2 = np.diag(S[:2])
VT_2 = VT[:2, :]
X_2D = np.dot(U_2, np.dot(Sigma_2, VT_2))

plt.figure(figsize=(10, 6))
plt.scatter(X_2D[:, 0], X_2D[:, 1], c='blue', marker='o')
plt.title('2D SVD Reduced Data')
plt.xlabel('Component 1')
plt.ylabel('Component 2')

plt.show()

# d = 3
U_3 = U[:, :3]
Sigma_3 = np.diag(S[:3])
VT_3 = VT[:3, :]
X_3D = np.dot(U_3, np.dot(Sigma_3, VT_3))

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_3D[:, 0], X_3D[:, 1], X_3D[:, 2], c='blue', marker='o')
ax.set_title('3D SVD Reduced Data')
ax.set_xlabel('Component 1')
ax.set_ylabel('Component 2')
ax.set_zlabel('Component 3')
plt.show()
