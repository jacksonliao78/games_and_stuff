import numpy as np
import matplotlib.pyplot as plt

# Given values
M_total = 73  # kg (includes books)
R_torso = 0.15  # m

# Moment of inertia for a solid disk (torso model when arms are close)
I_close = (1/2) * M_total * R_torso**2

# User-provided trial data
T_spread_avg = np.array([ (5.45 + 5.36)/2, (8 + 7.12)/2, (8.61 + 7.75)/2, (8.43 + 7.48)/2, (8.94 + 7.86)/2 ])
T_close_avg = np.array([ (2.13 + 2.21)/2, (2.43 + 2.65)/2, (3.06 + 3.25)/2, (2.63 + 2.75)/2, (3.35 + 3.23)/2 ])

# Compute angular velocities
w_spread = 2 * np.pi / T_spread_avg
w_close = 2 * np.pi / T_close_avg

# Compute I_spread using conservation of angular momentum
I_spread = I_close * (w_close / w_spread)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(range(1, 6), I_spread, marker='o', linestyle='-', label="I_spread")
plt.axhline(y=I_close, color='r', linestyle='--', label="I_close (constant)")

plt.xlabel("Trial Number")
plt.ylabel("Moment of Inertia (kg·m²)")
plt.title("Moment of Inertia for Spread vs. Close Arms")
plt.legend()
plt.grid(True)
plt.show()
