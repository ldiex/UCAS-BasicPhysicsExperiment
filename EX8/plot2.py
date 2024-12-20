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

N1 = 150
R1 = 2
l = 0.13
R2 = 50000
C = 10e-6
N2 = 150
S = 1.24e-4


H = [5.36, 6.24, 9.12, 13.8, 20.8, 25.6, 33.6, 48.0, 58.9, 70.0, 82.0, 104, 118, 132, 148, 156, 170, 182, 202]
B = [1.60, 1.96, 2.94, 4.40, 6.80, 7.80, 9.60, 12.0, 13.2, 14.8, 15.2, 16.0, 16.8, 16.8, 17.2, 17.2, 17.6, 17.6, 18.0]

H = [N1 / (R1 * l) * i / 1000 for i in H]
B = [R2 * C / (N2 * S) * i for i in B]

print(H)
print(B)

# Sort the data
sorted_indices = np.argsort(H)
H = np.array(H)[sorted_indices]
B = np.array(B)[sorted_indices]

# Create the scatter plot
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.scatter(H, B, marker='o')

# Create smooth curves
H_new = np.linspace(min(H), max(H), 300)
spl_B = make_interp_spline(H, B, k=2)
B1_smooth = spl_B(H_new)

# Plot smooth curves
plt.plot(H_new, B1_smooth)

# Add labels and title
plt.xlabel('$H$ (A/m)')
plt.ylabel('$B$ (mT)')
plt.title('Dynamic Magnetization Curve of Ferrite')


# Add a grid for better readability
plt.grid(True)

# Show Plot
plt.savefig('plot2.pdf')
