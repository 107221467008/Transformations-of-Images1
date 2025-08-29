#affine transformation
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


def affine_transform(points, A):
    """
    Apply affine transformation: [x', y', 1] = A * [x, y, 1]
    """
    homog = np.hstack([points, np.ones((points.shape[0], 1))])  # make homogeneous
    transformed = homog @ A.T
    return transformed[:, :2]

# Example affine transformation matrix (includes scaling, shear, translation)
A = np.array([
    [1.2, 0.5, 0.2],  # a11, a12, a13
    [0.3, 1.5, 0.1],  # a21, a22, a23
    [0,   0,   1  ]
])

# --- Apply affine transformation ---
transformed_square = affine_transform(square, A)

# --- Plotting ---
plt.figure(figsize=(6,6))

# Original square (black)
plt.plot(square[:,0], square[:,1], 'k-', linewidth=2, label="Original square")

# Transformed shape (red parallelogram/rectangle)
plt.plot(transformed_square[:,0], transformed_square[:,1], 'r-', linewidth=3, label="Affine transformed")

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
