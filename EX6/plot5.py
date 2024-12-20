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
    0.0761, 0.0407, 0.0239, 0.0149, 0.0128,
    0.0118, 0.0119, 0.0120, 0.0123, 0.0138,
    0.0174, 0.0342, 0.0672, 0.1130
]


x_list = [
    2.050, 2.150, 2.220, 2.231, 2.240,
    2.247, 2.250, 2.253, 2.256, 2.265,
    2.275, 2.320, 2.400, 2.600
]


# Data
y = np.array(y_list)
x = np.array(x_list).reshape(-1, 1)

# Define arccos function
def poly(x, a, b, c, d, e):
    return a * x ** 3 + b * x ** 2 + c * x + d

# Fit the data using curve_fit
popt, pcov = curve_fit(poly, x.flatten(), y, maxfev=10000)

# Plot the original data
plt.scatter(x, y, label='Data', color='blue', alpha=0.7)

# Plot the fitted curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = poly(x_fit, *popt)
plt.plot(x_fit, y_fit, label='Polynomial Fit', color='purple', alpha=0.7)

# Add labels and legend
plt.ylabel('$I_{\mathrm{max}}/\mathrm{mA}$')
plt.xlabel('$f/\mathrm{kHz}$')
plt.legend()
plt.title('$I \sim f$ Curve')
plt.grid(True)


# Show plot
plt.savefig('plot5.pdf')