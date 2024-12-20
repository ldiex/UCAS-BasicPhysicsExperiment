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
y = np.array([32.71, 45.72, 53.49, 56.89, 64.37])
x = np.array([2.48, 4.96, 7.44, 9.92, 12.40]).reshape(-1, 1)
x = np.log(x)
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
plt.title('Linear Regression of $\\log(f_1)$ vs $\\log T$')
plt.ylabel('$\\log(f_1)$')
plt.xlabel('$\\log T$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(0.9, 4.02, f"$\\log(f_1) = {slope:.2f}\\log T + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)

plt.savefig("plot2.pdf")

