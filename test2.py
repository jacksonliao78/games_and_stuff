# Given data
import numpy as np

M = 73  # kg (total mass with books)
R = 0.15  # m (torso radius when arms are close)

# Compute moment of inertia when arms are close (modeled as a disk)
I_close = (1/2) * M * R**2

# Given times for spread apart and close together
T_spread = np.array([(5.45 + 5.36) / 2, (8 + 7.12) / 2, (8.61 + 7.75) / 2, (8.43 + 7.48) / 2, (8.94 + 7.86) / 2])
T_close = np.array([(2.13 + 2.21) / 2, (2.43 + 2.65) / 2, (3.06 + 3.25) / 2, (2.63 + 2.75) / 2, (3.35 + 3.23) / 2])

# Compute angular velocities (ω = 2π / T)
omega_close = 2 * np.pi / T_close
omega_spread = 2 * np.pi / T_spread

# Compute total angular momentum L = I_close * omega_close
L = I_close * omega_close

# Compute moment of inertia when arms are spread out (I_spread = L / omega_spread)
I_spread = L / omega_spread

print( I_spread )
print(I_close)
