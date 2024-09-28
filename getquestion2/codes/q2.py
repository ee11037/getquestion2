import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Read the coordinates from the output file
with open('output.txt', 'r') as file:
    line = file.readline().strip()
    # Extract the coordinates
    coords = line[line.index('(')+1:line.index(')')].split()
    x_B, y_B, z_B = int(coords[0]), int(coords[1]), int(coords[2])

# Plotting in 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Define the line from the origin to point B
ax.plot([0, x_B], [0, y_B], [0, z_B], linestyle='--', linewidth=2, color='b', label='Line from Origin to B')

# Add an arrow at point B
ax.quiver(0, 0, 0, x_B, y_B, z_B, arrow_length_ratio=0.1, color='r')

# Add text labels
ax.text(0, 0, 0, 'Origin (0, 0, 0)', fontsize=12, ha='right', color='black')
ax.text(x_B, y_B, z_B, f'B({x_B}, {y_B}, {z_B})', fontsize=12, ha='left', color='black')

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Line from Origin to Point B in 3D')
ax.legend()

# Set limits (adjust as needed)
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Adjust the viewing angle for better visibility
ax.view_init(elev=20, azim=30)

plt.show()


