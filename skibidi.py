import math

# Data: (magnitude, angle in degrees)
data = [
    (21.375, 240),
    (22.545, 80),
    (0.4815, 135),
    (1.474, 130),
    (2.16, 130)
]

# Initialize variables for total x and y components of momentum
total_px = total_py = 0

# Loop through each momentum vector
for magnitude, angle_deg in data:
    angle_rad = math.radians(angle_deg)  # Convert angle to radians
    total_px += magnitude * math.cos(angle_rad)  # Calculate x component
    total_py += magnitude * math.sin(angle_rad)  # Calculate y component

# Calculate the total momentum magnitude
print(total_px, total_py)
total_momentum = math.sqrt(total_px**2 + total_py**2)

# Output the result
print("Total momentum magnitude:", total_momentum)
