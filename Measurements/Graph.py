#This code produces the bar graph for the measurements labimport matplotlib.pyplot as plt
# Graduated Cylinder
import matplotlib.pyplot as plt
measurements = [1, 2, 3, 4, 5]

# Density values (g/mL)
densities = [5.420, 3.187, 2.471, 2.103, 1.872]

# Calculate the average density
average = sum(densities) / len(densities)

# True density
true_density = 2.70

# Create the bar graph
plt.figure(figsize=(9, 6))

plt.bar(measurements, densities)

# Average density line
plt.axhline(
    average,
    linestyle="--",
    linewidth=2,
    label=f"Average = {average:.3f} g/mL"
)

# True density line
plt.axhline(
    true_density,
    linestyle=":",
    linewidth=2,
    label=f"True Density = {true_density:.2f} g/mL"
)

# Labels and title
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")
plt.title("Density Measurements")

# Show legend
plt.legend()

# Make the graph fit nicely
plt.tight_layout()

# Display the graph
plt.show()

# Print the average in the console
print(f"Average density = {average:.3f} g/mL")

import matplotlib.pyplot as plt

# Volumetric Pipettes
measurements = [1, 2, 3, 4, 5]

# Density values in g/mL
densities = [4.239, 2.615, 2.072, 1.801, 1.639]

# Calculate the average density
average = sum(densities) / len(densities)

# True density of water
true_density = 1.00

# Create the bar graph
plt.figure(figsize=(10, 6))

plt.bar(measurements, densities)

# Add average density line
plt.axhline(
    average,
    linestyle="--",
    linewidth=2,
    label=f"Average = {average:.3f} g/mL"
)

# Add true density line
plt.axhline(
    true_density,
    linestyle=":",
    linewidth=2,
    label=f"True Density = {true_density:.2f} g/mL"
)

# Labels and title
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")
plt.title("Density of Water with Volumetric Pipette")

# Add legend
plt.legend()

# Make the graph look neat
plt.tight_layout()

# Show the graph
plt.show()

# Print average in the console
print(f"Average density = {average:.3f} g/mL")

import matplotlib.pyplot as plt
import math

# Penny
measurements = [1, 2, 3, 4]

# Diameter, thickness, and mass for each measurement
diameters = [1.9, 1.9, 1.9, 1.9]       # cm
thicknesses = [0.1, 0.1, 0.1, 0.1]     # cm
masses = [2.51, 2.51, 2.51, 2.51]      # g

# Calculate radius
radius = [d / 2 for d in diameters]

# Calculate volume of each penny
volumes = [
    math.pi * r**2 * h
    for r, h in zip(radius, thicknesses)
]

# Calculate density
densities = [
    m / v
    for m, v in zip(masses, volumes)
]

# Calculate average density
average = sum(densities) / len(densities)

# True density of copper
true_density = 8.96  # g/cm^3

# Create the bar graph
plt.figure(figsize=(10, 6))

plt.bar(measurements, densities, label="Density")

# Average density line
plt.axhline(
    average,
    linestyle="--",
    linewidth=2,
    label=f"Average = {average:.2f} g/cm³"
)

# True density line
plt.axhline(
    true_density,
    linestyle=":",
    linewidth=2,
    label=f"True Density = {true_density:.2f} g/cm³"
)

# Add labels
plt.xlabel("Measurement")
plt.ylabel("Density (g/cm³)")
plt.title("Penny")

# Add legend
plt.legend()

# Make graph neat
plt.tight_layout()

# Show graph
plt.show()

# Print calculations
print("Penny Density Measurements")
print("---------------------------")

for i in range(len(measurements)):
    print(
        f"Measurement {measurements[i]}: "
        f"Volume = {volumes[i]:.3f} cm³, "
        f"Density = {densities[i]:.2f} g/cm³"
    )

print("---------------------------")
print(f"Average density = {average:.2f} g/cm³")
print(f"True density = {true_density:.2f} g/cm³")