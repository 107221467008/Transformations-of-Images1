#projective transformation
import numpy as np
import matplotlib.pyplot as plt

# --- Original square coordinates ---
square = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
    [0, 0]  # closing the square
])


def projective_transform(points, H):
    """
    Apply projective transformation: [x', y', w] = H * [x, y, 1]
    Normalize by dividing with w
    """
    homog = np.hstack([points, np.ones((points.shape[0], 1))])  # homogeneous
    transformed = homog @ H.T
    transformed /= transformed[:, 2].reshape(-1, 1)  # normalize by w
    return transformed[:, :2]

# Example projective transformation matrix (creates perspective distortion)
H = np.array([
    [1, 0.3, 0.2],
    [0.2, 1, 0.1],
    [0.001, 0.002, 1]  # perspective row (if 0, reduces to affine)
])

# --- Apply transformation ---
transformed_square = projective_transform(square, H)

# --- Plotting ---
plt.figure(figsize=(6,6))

# Original square (black)
plt.plot(square[:,0], square[:,1], 'k-', linewidth=2, label="Original square")

# Transformed quadrilateral (red trapezoid-like)
plt.plot(transformed_square[:,0], transformed_square[:,1], 'r-', linewidth=3, label="Projective transformed")

# Draw arrows (axes)
plt.axhline(0, color='k', linestyle='-', linewidth=1)
plt.axvline(0, color='k', linestyle='-', linewidth=1)
plt.arrow(0, 0, 2, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
plt.arrow(0, 0, -2, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
plt.arrow(0, 0, 0, 2, head_width=0.1, head_length=0.1, fc='k', ec='k')
plt.arrow(0, 0, 0, -2, head_width=0.1, head_length=0.1, fc='k', ec='k')

# Settings
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(False)
plt.axis('off')
plt.show()
