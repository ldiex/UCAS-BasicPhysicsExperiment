
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import  PolynomialFeatures
import matplotlib

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
matplotlib.rcParams['mathtext.fontset'] = 'stix'
# Data
x = np.array([20, 25, 30, 35, 45, 50, 55, 60]).reshape(-1, 1)
y = np.array([590.620, 588.321, 586.620, 585.521, 585.321, 586.121, 587.221 , 588.521])

# Fit a polynomial regression model
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)
model = LinearRegression()
model.fit(x_poly, y)

# Generate predictions from x_min to x_max with 1000 points
x_min = x.min()
x_max = x.max()
x_range = np.linspace(x_min, x_max, 1000)
x_range_poly = poly.fit_transform(x_range.reshape(-1, 1))
y_pred = model.predict(x_range_poly)

# Find the minimum value of y_pred
y_min = y_pred.min()
x_argmin = x_range[np.argmin(y_pred)]

# Print the formula of the polynomial
print(f"Polynomial: {model.intercept_} + {model.coef_[1]}x + {model.coef_[2]}x^2")

# Print the minimum value of y_pred
print(f"Minimum value of y_pred: {y_min}")
print(f"Value of x at minimum y_pred: {x_argmin}")

# Plotting
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_range, y_pred, color='red', label='Polynomial Regression')
plt.title('Polynomial Regression of $f_1$ vs $x$ ')
plt.ylabel('$f_1(\mathrm{Hz})$')
plt.xlabel('$x(\mathrm{mm})$')
plt.legend()
plt.grid()

# Add the formula equation to the plot
plt.text(43, 589.6, f"$f_1 = {model.intercept_:.2f}  {model.coef_[1]:.2f}x + {model.coef_[2]:.2f}x^2$", fontsize=12)

plt.savefig("plot4.pdf")
