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
y = np.array([0.0, 13.9, 27.4, 40.9, 54.5, 68.1, 81.9])
x = np.array([0, 50, 100, 150, 200, 250, 300]).reshape(-1, 1)

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
plt.title('Linear Regression of $V_H$ vs $I_M$')
plt.xlabel('$I_M(\mathrm{mA})$')
plt.ylabel('$V_H(\mathrm{mV})$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(0, 65, f"$V_H = {slope:.2f}I_M + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)

plt.savefig("plot2.pdf")

