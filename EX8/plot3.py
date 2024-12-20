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

mu_0 = 1 * np.pi * 1e-7
MU = [B[i] / H[i] / mu_0 / 10000 for i in range(len(H))]

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
plt.savefig('plot3.pdf')
