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
y = np.array([0.0, 27.5, 54.6, 81.6, 108.9, 136.0, 163.2])
x = np.array([0.00, 0.50, 1.00, 1.50, 2.00, 2.50, 3.00]).reshape(-1, 1)

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
plt.title('Linear Regression of $V_H$ vs $I_S$')
plt.xlabel('$I_S(\mathrm{mA})$')
plt.ylabel('$V_H(\mathrm{mV})$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(0, 125, f"$V_H = {slope:.2f}I_S + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)

plt.savefig("plot1.pdf")

