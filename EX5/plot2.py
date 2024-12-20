import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
import matplotlib

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
matplotlib.rcParams['mathtext.fontset'] = 'stix'
plt.style.use('seaborn-v0_8-paper')

# Data
y = np.array([1582.55, 1626.10, 1668.55, 1710.22, 1750.53])
x = np.array([217.2, 229.37, 241.73, 254.19, 266.50]).reshape(-1, 1)
y = y / 1000
x = x / 1000
y = y * y
# Perform linear regression
model = Ridge(alpha=1e-5)
model.fit(x, y)
# Get the slope and intercept of the line best fit
slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope: {slope}")

# Get the R^2 value
r_squared = model.score(x, y)

# Generate predictions
y_pred = model.predict(x)

# Plotting
plt.scatter(x, y, color='blue', alpha=0.7,  label='Data Points')
plt.plot(x, y_pred, color='purple', alpha = 0.7, label='Linear Regression Line')
plt.title('Linear Regression (Ridge with $\\alpha = 10^{-5}$) of $T^2$ vs $m$')
plt.ylabel('$T^2 (\\mathrm{s^2})$')
plt.xlabel('$m (\\mathrm{kg})$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(0.235, 2.55, f"$T^2 = {slope:.2f}m + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)

plt.savefig("plot2.pdf")


