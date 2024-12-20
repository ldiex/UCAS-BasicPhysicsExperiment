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


H = [11.53, 23.08, 34.61, 46.15, 57.69, 69.23, 80.77, 92.31, 103.85, 115.38]
MU = [4642, 4467, 3761, 2288, 1649, 1251, 983, 712, 543, 417]

print(H)
print(MU)

# Fit a polynomial regression model
degree = 6
coefficients = np.polyfit(H, MU, degree)
polynomial = np.poly1d(coefficients)

# Generate x values for the polynomial line
H_poly = np.linspace(min(H), max(H), 500)
MU_poly = polynomial(H_poly)

# Plot the original data points
plt.scatter(H, MU, color='blue', label='Data points')

# Plot the polynomial regression line
plt.plot(H_poly, MU_poly, color='red', label=f'Polynomial fit (degree {degree})')

# Add legend
plt.legend()

# Add labels and title
plt.xlabel('$H$ (A/m)')
plt.ylabel('$\mu$')
plt.title('$\mu$ vs $H$ of Ferrite')

# print the polynomial equation
print(polynomial)

# Add a grid for better readability
plt.grid(True)

# Show Plot
plt.savefig('plot4.pdf')
