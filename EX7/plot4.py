import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib
from matplotlib.ticker import FuncFormatter

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
matplotlib.rcParams['mathtext.fontset'] = 'stix'
plt.style.use('seaborn-v0_8-paper')


data_u1 = [-0.00160994, 0.0991723, 0.198345, 0.298483, 0.3983, 0.498116, 
         0.598577, 0.699037, 0.797888, 0.898992, 0.999453, 1.0983, 
         1.19844, 1.29826, 1.3984, 1.49822, 1.59868, 1.69882, 1.79799, 
         1.89909, 1.99891]

data_u1 = [-_ for _ in data_u1]

data_i1 = [-1.60E-06, -4.82E-06, -4.82E-06, -4.82E-06, -1.60E-06, 1.62E-06, 
         -4.82E-06, -4.82E-06, 4.84E-06, -4.82E-06, -4.82E-06, -1.60E-06, 
         -4.82E-06, -1.60E-06, -1.60E-06, 1.62E-06, -1.60E-06, -4.82E-06, 
         1.62E-06, -8.04E-06, -4.82E-06]


# Data
y = np.array(data_u1)
x = np.array(data_i1).reshape(-1, 1)

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
# plt.plot(x, y_pred, color='purple', alpha = 0.7, label='Linear Regression Line')
plt.title('$U$ vs $I$')
plt.ylabel('$U (\\mathrm{V})$')
plt.xlabel('$I (\\mathrm{A})$')
plt.legend()
plt.grid()

# Add the equation of the line
# plt.text(0.001, 0.26, f"$U = {slope:.2f}I + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)
print(f"Slope: {slope}, Intercept: {intercept}, R^2: {r_squared}")
plt.savefig("plot4.pdf")


