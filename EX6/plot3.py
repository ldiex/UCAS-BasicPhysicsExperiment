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

y_list = [-79.70, -72.76, -63.94, -33.73, -19.35, 3.24, 4.86, 
          9.73, 12.99, 30.99, 42.59, 66.82, 77.76, 86.11]

x_list = [
    2.050, 2.150, 2.220, 2.231, 2.240,
    2.247, 2.250, 2.253, 2.256, 2.265,
    2.275, 2.320, 2.400, 2.600
]


# Data
y = np.array(y_list)
x = np.array(x_list).reshape(-1, 1)

# Define arccos function
def arccot_func(x, a, b, c, d):
    return a * np.arctan(b * (x - c)) + d

# Fit the data using curve_fit
popt, pcov = curve_fit(arccot_func, x.flatten(), y)

# Plot the original data
plt.scatter(x, y, label='Data', color='blue', alpha=0.7)

# Plot the fitted curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = arccot_func(x_fit, *popt)
plt.plot(x_fit, y_fit, label='Arctan Fit', color='purple', alpha=0.7)

# Add labels and legend
plt.ylabel('$\Delta \phi/^\circ$')
plt.xlabel('$f/\mathrm{kHz}$')
plt.legend()
plt.title('$\Delta \phi \sim f$ Curve')
plt.grid(True)

# Show plot
plt.savefig('plot3.pdf')