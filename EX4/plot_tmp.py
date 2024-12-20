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
y = np.array([2209.2, 1789.4, 1461.5, 1199.5, 989.1])
x = np.array([30, 35, 40, 45, 50]).reshape(-1, 1)
y = np.log(y)
x = 1 / (x + 273)
# Perform linear regression
model = LinearRegression()
model.fit(x, y)
# Get the slope and intercept of the line best fit
slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"Exp Intercept: {np.exp(intercept)}")

# Get the R^2 value
r_squared = model.score(x, y)
print(f"R^2: {r_squared}")
# Generate predictions
y_pred = model.predict(x)

# Plotting
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred, color='red', label='Linear Regression Line')
plt.title('Linear Regression of $\\log(2L)$ vs $\\log f$')
plt.ylabel('$\\log(2L)$')
plt.xlabel('$\\log f$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(3.8, 6.9, f"$\\log(2L) = {slope:.2f}\\log f + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)

plt.savefig("plot1.pdf")

