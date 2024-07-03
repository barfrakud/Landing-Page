import matplotlib.pyplot as plt

# List of coordinates
coordinates = [
    (18.833196, 49.510261),
    (18.837434, 49.526952),
    (18.83454, 49.547623),
    (18.820174, 49.590256),
    (18.81573, 49.599299),
    (18.803947, 49.616766),
    (18.799297, 49.626378),
    (18.792579, 49.660794),
    (18.788444, 49.668597),
    (18.773458, 49.675832),
    (18.757852, 49.674075),
    (18.742246, 49.669683),
    (18.727673, 49.668907),
    (18.715064, 49.673817),
    (18.695427, 49.688854),
    (18.682404, 49.695779),
    (18.668142, 49.69857),
    (18.637343, 49.700327),
    (18.62401, 49.706373),
    (18.617706, 49.713866),
    (18.60768, 49.74296),
]

# Extract x and y coordinates
x_coords, y_coords = zip(*coordinates)

# Create a scatter plot with lines connecting adjacent points
for i in range(len(x_coords) - 1):
    plt.plot([x_coords[i], x_coords[i + 1]], [y_coords[i], y_coords[i + 1]], "ro-")

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Poland Borders with Connecting Lines")
plt.grid(True)
plt.show()
