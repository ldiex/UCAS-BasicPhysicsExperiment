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
y = np.array([0.462, 0.470, 0.474, 0.485])
x = np.array([1, 3, 5, 10]).reshape(-1, 1)

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
plt.title('Linear Regression (Least Squares Method) of $\\bar{v}$ vs $d$')
plt.ylabel('$\\bar{v} (\\mathrm{m^2 \\cdot s^{-2}})$')
plt.xlabel('$d (\\mathrm{cm})$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(4.5, 0.4660, f"$\\bar v = {slope:.5f}d + {intercept:.3f}$, $R^2 = {r_squared:.2f}$", fontsize=12)
print(f"Slope: {slope}, Intercept: {intercept}, R^2: {r_squared}")
plt.savefig("plot7.pdf")


