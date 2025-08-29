#euclidean transformation
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

# --- Euclidean transformation function (rotation + translation) ---
def euclidean_transform(points, theta, tx=0, ty=0, cx=0, cy=0):
    """
    Apply Euclidean transformation: rotation about (cx, cy) + translation
    """
    # Rotation matrix
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    
    # Translate to origin around (cx, cy), apply rotation, then translate back + (tx, ty)
    shifted = points - np.array([cx, cy])
    rotated = shifted @ R.T
    transformed = rotated + np.array([cx + tx, cy + ty])
    return transformed

# --- Apply Euclidean transformation ---
theta = np.pi / 6   # 30 degrees rotation
tx, ty = 0.5, 0.3   # translation
cx, cy = 0.5, 0.5   # rotate around center of square

transformed_square = euclidean_transform(square, theta, tx, ty, cx, cy)

# --- Plotting ---
plt.figure(figsize=(6,6))

# Original square (black)
plt.plot(square[:,0], square[:,1], 'k-', linewidth=2, label="Original square")

# Transformed square (blue)
plt.plot(transformed_square[:,0], transformed_square[:,1], 'b-', linewidth=3, label="Euclidean transformed")

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
