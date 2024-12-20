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
    1.555, 2.180, 2.855, 4.630, 4.575,
    4.780, 4.805, 4.815, 4.790, 4.745,
    4.460, 3.715, 2.805, 1.785, 0.935
]

x_list = [
    1.88, 2.00, 2.08, 2.15, 2.19,
    2.22, 2.24, 2.25, 2.26, 2.28,
    2.30, 2.36, 2.43, 2.62, 3.18
]

# Data
y = np.array(y_list)
x = np.array(x_list).reshape(-1, 1)

# Define Gaussian function
def gaussian(x, a, b, c, d):
    return a * np.exp(-((x - b) ** 2) / (2 * c ** 2)) + d

# Fit the data
popt, pcov = curve_fit(gaussian, x.flatten(), y)

plt.figure(figsize=(6, 3))

# Plot the data
plt.scatter(x, y, label='Data', color='blue', alpha=0.7)

# Plot the Gaussian fit
x_fit = np.linspace(min(x), max(x), 1000)
y_fit = gaussian(x_fit, *popt)
plt.plot(x_fit, y_fit, color='purple', label='Gaussian fit', alpha=0.7)

# Add labels and legend
plt.ylabel('$I_{\mathrm{max}}/\mathrm{mA}$')
plt.xlabel('$f/\mathrm{kHz}$')
plt.legend()
plt.title('$I \sim f$ Curve')

plt.grid(True)

# Print the fit function
print(f'Fit function: I(f) = {popt[0]:.3f} * exp(-((f - {popt[1]:.3f}) ** 2) / (2 * {popt[2]:.3f} ** 2)) + {popt[3]:.3f}')

# Get I max
I_max = popt[0] + popt[3]
I_th = I_max / np.sqrt(2)
# Get Delta f = f_2 - f_1, where I(f_1) = I(f_2) = I_th
f_1 = np.min(x_fit[np.where(y_fit > I_th)])
f_2 = np.max(x_fit[np.where(y_fit > I_th)])
Delta_f = f_2 - f_1
print(f'I_max = {I_max:.3f} mA')
print(f'I_th = {I_th:.3f} mA')
print(f'Delta f = {Delta_f:.3f} kHz')

# Show plot
plt.savefig('plot1.pdf')