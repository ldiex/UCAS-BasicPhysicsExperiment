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
y = np.array([0.768, 0.966, 1.034, 1.060, 1.082])
x = np.array([30.2, 35.1, 40.2, 45.0, 50.0]).reshape(-1, 1)
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
plt.title('Linear Regression of $E_x$ vs $t$')
plt.ylabel('$E_x (\\mathrm{mV})$')
plt.xlabel('$t \\mathrm{(^\\circ C)}$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(38, 0.81, f"$E_x = {slope:.2f}t + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)

plt.savefig("plot3.pdf")

