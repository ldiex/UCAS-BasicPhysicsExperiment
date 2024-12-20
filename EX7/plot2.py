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

data_u = [0, 0.0148115, 0.0318768, 0.0479762, 0.0640757, 0.0798531, 0.0965965, 
         0.112696, 0.128473, 0.144895, 0.160994, 0.176128, 0.192549, 0.209615, 
         0.225392, 0.240526, 0.257269, 0.274657, 0.289468, 0.305568, 0.321345]

data_i = [-1.77E-05, 0.000326826, 0.000661694, 0.000996561, 0.00133143, 
         0.00166952, 0.00200438, 0.00233925, 0.00267412, 0.00301221, 
         0.00334708, 0.00368838, 0.00402003, 0.00435168, 0.00468655, 
         0.00503108, 0.00536273, 0.00569115, 0.0060389, 0.00637055, 
         0.00671186]



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
plt.text(0.001, 0.26, f"$U = {slope:.2f}I + {intercept:.2f}$, $R^2 = {r_squared:.2f}$", fontsize=12)
print(f"Slope: {slope}, Intercept: {intercept}, R^2: {r_squared}")
plt.savefig("plot2.pdf")


