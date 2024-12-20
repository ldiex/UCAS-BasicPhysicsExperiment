
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
x = np.array([3.895, 3.802, 3.710, 3.581, 3.439, 3.318, 3.171, 3.034]).reshape(-1, 1)
y = np.array([19, 38, 57, 77, 86, 114, 131, 147])

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
plt.title('Linear Regression of $\\Delta Z_i$ vs $U_i$ ')
plt.xlabel('$\\Delta Z_i(\mathrm{mm})$')
plt.ylabel('$U_i(\mathrm{mV})$')
plt.legend()
plt.grid()
plt.savefig("plot3.pdf")
