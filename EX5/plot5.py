import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
matplotlib.rcParams['mathtext.fontset'] = 'stix'
plt.style.use('seaborn-v0_8-paper')

# Data
y = np.array([38.55, 57.56, 76.09, 96.34, 115.83])
x = np.array([10, 15, 20, 25, 30]).reshape(-1, 1)
y = y / 100
x = x / 100
x = x * x
y = y * y
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
plt.scatter(x, y, color='blue', alpha=0.7,  label='Data Points')
plt.plot(x, y_pred, color='purple', alpha = 0.7, label='Linear Regression Line')
plt.title('Linear Regression (Least Squares Method) of $v^2$ vs $A^2$')
plt.ylabel('$v^2 (\\mathrm{m^2 \\cdot s^{-2}})$')
plt.xlabel('$A^2 (\\mathrm{m^2})$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(0.015, 1.1, f"$v^2 = {slope:.2f}A^2 + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)
print(f"Slope: {slope}, Intercept: {intercept}, R^2: {r_squared}")
plt.savefig("plot5.pdf")


