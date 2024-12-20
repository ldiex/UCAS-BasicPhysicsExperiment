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
y = np.array([13.80, 20.68, 27.56, 34.35, 41.08, 47.92, 54.72])
x = np.array([38.0, 57.1, 75.4, 94.4, 113.3, 131.6, 150.5]).reshape(-1, 1)
x = x * 1e-3
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
plt.title('Linear Regression of $V_{H-\mathrm{AC}}$ vs $I_{S-\mathrm{AC}} B$')
plt.ylabel('$V_{H-\mathrm{AC}}(\mathrm{mV})$')
plt.xlabel('$I_{S-\mathrm{AC}} B(\mathrm{mA \cdot T})$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(0.04, 45, f"$V_H = {slope:.2f}I_S B {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)

plt.savefig("plot6.pdf")

