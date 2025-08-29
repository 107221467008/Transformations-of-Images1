#similarity transformation
import numpy as np
import matplotlib.pyplot as plt

# --- Original square coordinates ---
square = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
    [0, 0]  # Closing the square
])


def similarity_transform(points, k=1.5, theta=np.pi/4, tx=0, ty=0):
    """
    Apply similarity transformation: scaling, rotation, translation
    """
    # Transformation matrix
    T = np.array([
        [k*np.cos(theta), -k*np.sin(theta), tx],
        [k*np.sin(theta),  k*np.cos(theta), ty],
        [0, 0, 1]
    ])
    
    # Convert to homogeneous coords
    homog = np.hstack([points, np.ones((points.shape[0], 1))])
    
    # Apply transformation
    transformed = homog @ T.T
    return transformed[:, :2]

# --- Apply transformation ---
transformed_square = similarity_transform(square, k=1.5, theta=0, tx=0, ty=0)

# --- Plotting ---
plt.figure(figsize=(5,5))

# Original square (black)
plt.plot(square[:,0], square[:,1], 'k-', linewidth=2)

# Transformed square (red)
plt.plot(transformed_square[:,0], transformed_square[:,1], 'r-', linewidth=3)

# Draw arrows (axes)
plt.axhline(0, color='k', linestyle='-', linewidth=1)
plt.axvline(0, color='k', linestyle='-', linewidth=1)
plt.arrow(0, 0, 2, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
plt.arrow(0, 0, -2, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
plt.arrow(0, 0, 0, 2, head_width=0.1, head_length=0.1, fc='k', ec='k')
plt.arrow(0, 0, 0, -2, head_width=0.1, head_length=0.1, fc='k', ec='k')

# Settings
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(False)
plt.axis('off')
plt.show()
