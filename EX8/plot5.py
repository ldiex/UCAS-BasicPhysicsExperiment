import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.interpolate import make_interp_spline

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
matplotlib.rcParams['mathtext.fontset'] = 'stix'
plt.style.use('seaborn-v0_8-paper')

I = [0, 30, 59.9, 90.4, 120.0, 149.9, 180.0, 210.5, 240.8, 269.9, 300.7, 330.0, 360.0, 390.2, 419.9, 449.9, 480.3, 510.3, 540.1, 571.0]
H = [0.0, 204.8, 403.7, 603.7, 767.6, 920.0, 1067.1, 1207.3, 1326.8, 1442.6, 1563.6, 1679.2, 1798.7, 1920.5, 2043.2, 2173.5, 2311.0, 2436.9, 2601.8, 2761.9]


# Sort the data
sorted_indices = np.argsort(I)
H = np.array(H)[sorted_indices]
I = np.array(I)[sorted_indices]

# Create the scatter plot
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.scatter(I, H, marker='o')

# Create smooth curves
I_new = np.linspace(min(I), max(I), 300)
spl_H = make_interp_spline(I, H, k=2)
H_smooth = spl_H(I_new)

# Plot smooth curves
plt.plot(I_new, H_smooth)

# Add labels and title
plt.xlabel('$I$ (mA)')
plt.ylabel('$H$ (mT)')

plt.title('The Starting Magnetization Curve of a Mold Steel Sample')


# Add a grid for better readability
plt.grid(True)

# Show Plot
plt.savefig('plot5.pdf')
