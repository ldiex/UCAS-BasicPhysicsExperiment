
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
x = np.array([250, 500, 750, 1000, 1250, 1500, 1750, 2000]).reshape(-1, 1)
y = np.array([0.35, 0.555, 0.74, 0.93, 1.08, 1.25, 1.395, 1.52])

# Perform linear regression
model = LinearRegression()
model.fit(x, y)
# Get the slope and intercept of the line best fit
slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope: {slope}")
# Generate predictions
y_pred = model.predict(x)

# Plotting
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred, color='red', label='Linear Regression Line')
plt.title('Linear Regression of $M_i$ vs $\\bar{l}_i$')
plt.xlabel('$M_i(\mathrm{g})$')
plt.ylabel('$\\bar{l}_i(\mathrm{mm})$')
plt.legend()
plt.grid()
plt.savefig("plot1.pdf")
