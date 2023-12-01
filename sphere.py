import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

# input returns strings so make sure to cast them to ints!
choice = int(input("How do you want to generate your graph? \n 1. Normalized Vectors \n 2. Spherical Coordinates \n"))

while(int(choice) != 1 and int(choice) != 2):
    choice = input("Pick again!\n")

x_sphere = None
y_sphere = None
z_sphere = None

if(choice == 1):
        # Generates random x, y, z values
        x = np.random.randn(1000)
        y = np.random.randn(1000)
        z = np.random.randn(1000)

        # These values are then put into a vector
        vectors = np.vstack((x, y, z)).T

        # We then normalize the vectors so they are on a sphere
        normalized_vectors = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)

        # We then take the x, y, and z components of each vector so they can be put on a sphere
        x_sphere = normalized_vectors[:, 0]
        y_sphere = normalized_vectors[:, 1]
        z_sphere = normalized_vectors[:, 2]

elif(choice == 2):
    # Generates random spherical coordinates
    phi = np.arccos(1-2*np.random.rand(1000))
    theta = np.random.uniform(0, 2*np.pi, 1000)

    # Converts spherical coordinates to Cartesian coordinates
    x_sphere = np.sin(phi) * np.cos(theta)
    y_sphere = np.sin(phi) * np.sin(theta)
    z_sphere = np.cos(phi)

# Setting up the Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Plotting the points on the sphere
ax.scatter(x_sphere, y_sphere, z_sphere, s=5, alpha=0.6)

plt.show()
