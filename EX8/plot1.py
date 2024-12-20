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

# Data from the table
H = [209, 68, 18, 0, -12, -48, -212]
B1 = [20.2, 15.6, 8.4, 3.6, 0, -9.6, -20]
B2 = [20.2, 13.6, 0, -4.8, -8.1, -13.2, -20]

H = [N1 / (R1 * l) * i / 1000 for i in H]
B1 = [R2 * C / (N2 * S) * i for i in B1]
B2 = [R2 * C / (N2 * S) * i for i in B2] 

print(H)
print(B1)
print(B2)

# Sort the data
sorted_indices = np.argsort(H)
H = np.array(H)[sorted_indices]
B1 = np.array(B1)[sorted_indices]
B2 = np.array(B2)[sorted_indices]

# Create the scatter plot
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.scatter(H, B1, marker='o')
plt.scatter(H, B2, marker='o')

# Create smooth curves
H_new = np.linspace(min(H), max(H), 300)
spl_B1 = make_interp_spline(H, B1, k=1)
spl_B2 = make_interp_spline(H, B2, k=1)
B1_smooth = spl_B1(H_new)
B2_smooth = spl_B2(H_new)

# Plot smooth curves
plt.plot(H_new, B1_smooth)
plt.plot(H_new, B2_smooth)

# Add labels and title
plt.xlabel('$H$ (A/m)')
plt.ylabel('$B$ (mT)')
plt.title('Saturation Dynamic Hysteresis Loop of Ferrite')


# Add a grid for better readability
plt.grid(True)

# Show Plot
plt.savefig('plot1.pdf')
