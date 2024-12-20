import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
matplotlib.rcParams['mathtext.fontset'] = 'stix'
# Data
y = np.array([32.75, 43.89, 43.04, 33.71, 33.35])
x = np.array([3.50, 1.53, 2.15, 3.80, 3.68]).reshape(-1, 1)
x = np.log(x/1000)
y = np.log(y)
# Perform linear regression
model = LinearRegression()
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
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred, color='red', label='Linear Regression Line')
plt.title('Linear Regression of $\\log(f_1)$ vs $\\log \\mu$')
plt.ylabel('$\\log(f_1)$')
plt.xlabel('$\\log \\mu$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(-6.35, 3.52, f"$\\log(f_1) = {slope:.2f}\\log \\mu + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)

plt.savefig("plot3.pdf")

