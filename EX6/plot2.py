import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib
from scipy.optimize import curve_fit

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
matplotlib.rcParams['mathtext.fontset'] = 'stix'
plt.style.use('seaborn-v0_8-paper')

y_list = [
    -86.78, -72.40, -60.86, -41.57, -28.73, -13.32, -3.72,
     2.10,   7.00,  16.35,  27.43,  49.20,  57.22,  65.47,  69.94
]

x_list = [
    1.88, 2.00, 2.08, 2.15, 2.19,
    2.22, 2.24, 2.25, 2.26, 2.28,
    2.30, 2.36, 2.43, 2.62, 3.18
]

# Data
y = np.array(y_list)
x = np.array(x_list).reshape(-1, 1)

# Define arccos function
def arctan_func(x, a, b, c, d):
    return a * np.arctan(b * (x - c)) + d

# Fit the data using curve_fit
popt, pcov = curve_fit(arctan_func, x.flatten(), y)

# Plot the original data
plt.scatter(x, y, label='Data', color='blue', alpha=0.7)

# Plot the fitted curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = arctan_func(x_fit, *popt)
plt.plot(x_fit, y_fit, label='Arctan Fit', color='purple', alpha=0.7)

# Add labels and legend
plt.ylabel('$\Delta \phi/^\circ$')
plt.xlabel('$f/\mathrm{kHz}$')
plt.legend()
plt.title('$\Delta \phi \sim f$ Curve')
plt.grid(True)

# Show plot
plt.savefig('plot2.pdf')