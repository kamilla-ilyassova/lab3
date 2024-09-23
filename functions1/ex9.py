import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Example:
radius = 5
volume = sphere_volume(radius)
print(f"Volume of the sphere is {volume:.2f}.")