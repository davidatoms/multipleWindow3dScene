import numpy as np
import math

# Function to apply Möbius transformation
def moebius_transform(Pt, circle_radius=1, p=0, q=1, t=0.5):
    # Normalize point to unit circle if using a specific circle
    Pt /= circle_radius

    xa, ya, za = Pt

    # Reverse stereographic projection to 4D hypersphere
    denom = 1 + xa ** 2 + ya ** 2 + za ** 2
    xb = 2 * xa / denom
    yb = 2 * ya / denom
    zb = 2 * za / denom
    wb = (-1 + xa ** 2 + ya ** 2 + za ** 2) / denom

    # Rotate hypersphere by amount t
    xc = +(xb) * (math.cos(p * t)) + (yb) * (math.sin(p * t))
    yc = -(xb) * (math.sin(p * t)) + (yb) * (math.cos(p * t))
    zc = +(zb) * (math.cos(q * t)) - (wb) * (math.sin(q * t))
    wc = +(zb) * (math.sin(q * t)) + (wb) * (math.cos(q * t))

    # Project stereographically back to flat 3D
    xd = xc / (1 - wc)
    yd = yc / (1 - wc)
    zd = zc / (1 - wc)

    # Transform back to input circle
    P = np.array([xd, yd, zd]) * circle_radius

    return P

# Example usage
Pt = np.array([0.5, 0.5, 0.5])  # Input point in 3D
transformed_P = moebius_transform(Pt, circle_radius=1, p=0, q=1, t=0.5)
print("Transformed Point:", transformed_P)

import matplotlib.pyplot as plt

# Generate some sample points to transform
points = [np.array([x, y, 0]) for x in np.linspace(-1, 1, 10) for y in np.linspace(-1, 1, 10)]
transformed_points = [moebius_transform(pt, circle_radius=1, p=0, q=1, t=0.5) for pt in points]

# Plot original and transformed points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([pt[0] for pt in points], [pt[1] for pt in points], [pt[2] for pt in points], color='blue', label='Original')
ax.scatter([pt[0] for pt in transformed_points], [pt[1] for pt in transformed_points], [pt[2] for pt in transformed_points], color='red', label='Transformed')
ax.legend()
plt.show()

