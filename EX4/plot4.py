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
y = np.array([58.2, 59.4, 60.5, 61.5, 62.7])
x = np.array([30, 35, 40, 45, 50]).reshape(-1, 1)
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
plt.title('Linear Regression of $R_x$ vs $t$')
plt.ylabel('$R_x (\\mathrm{\\Omega})$')
plt.xlabel('$t \\mathrm{(^\\circ C)}$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(30.5, 61.5, f"$R_x = {slope:.2f}t + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)

plt.savefig("plot4.pdf")

