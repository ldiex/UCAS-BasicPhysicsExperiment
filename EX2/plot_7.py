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
x = np.array([-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25]).reshape(-1, 1)
y = np.array([0.139, 0.143, 0.146, 0.148, 0.149, 0.149, 0.148, 0.147, 0.143, 0.140, 0.136])
y1 = np.array([0.130, 0.135, 0.138, 0.141, 0.143, 0.144, 0.143, 0.142, 0.140, 0.138, 0.134])

# Fit a polynomial regression model
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)
model = LinearRegression()
model.fit(x_poly, y)

poly1 = PolynomialFeatures(degree=2)
x_poly1 = poly1.fit_transform(x)
model1 = LinearRegression()
model1.fit(x_poly1, y1)

# Generate predictions from x_min to x_max with 1000 points
x_min = x.min()
x_max = x.max()
x_range = np.linspace(x_min, x_max, 1000)
x_range_poly = poly.fit_transform(x_range.reshape(-1, 1))
y_pred = model.predict(x_range_poly)

x_range_poly1 = poly1.fit_transform(x_range.reshape(-1, 1))
y_pred1 = model1.predict(x_range_poly1)

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
plt.scatter(x, y1, color='purple', label='Theoretical Points')
plt.plot(x_range, y_pred, color='red', label='Regression of Data Points')
plt.plot(x_range, y_pred1, color='orange', label='Regression of Theoretical Points')
plt.title('Polynomial Regression of $B$ vs $X$ ')
plt.ylabel('$B(\mathrm{mT})$')
plt.xlabel('$X(\mathrm{mm})$')
plt.legend()
plt.grid()

plt.savefig("plot7.pdf")
