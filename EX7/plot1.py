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


data_u = [-0.00128795, 0.450462, 0.902535, 1.35396, 1.80604, 2.25876, 2.71052, 
         3.16164, 3.6134, 4.06549, 4.51758, 4.96806, 5.41984, 5.87226, 
         6.32533, 6.7768, 7.22794, 7.68006, 8.13154, 8.58271, 9.03516]

data_i = [-8.04E-06, 0.000474941, 0.000951483, 0.00143125, 0.00190779, 
         0.00238111, 0.00285121, 0.00333742, 0.00381396, 0.00429694, 
         0.00476383, 0.00524681, 0.00572979, 0.00620312, 0.00667644, 
         0.0071562, 0.00763919, 0.00810929, 0.00858906, 0.00907526, 
         0.00954214]


# Data
y = np.array(data_u)
x = np.array(data_i).reshape(-1, 1)

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
plt.title('Linear Regression (Least Squares Method) of $U$ vs $I$')
plt.ylabel('$U (\\mathrm{V})$')
plt.xlabel('$I (\\mathrm{A})$')
plt.legend()
plt.grid()

# Add the equation of the line
plt.text(0.001, 7, f"$U = {slope:.2f}I + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)
print(f"Slope: {slope}, Intercept: {intercept}, R^2: {r_squared}")
plt.savefig("plot1.pdf")


