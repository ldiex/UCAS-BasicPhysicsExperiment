import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def create_fourier_features(x, n_harmonics):
    """Create Fourier features up to n_harmonics."""
    # Convert to radians and normalize to [0, 2π]
    x_rad = (x * 2 * np.pi / 360).reshape(-1, 1)
    
    features = [np.ones(len(x))]  # Constant term
    for i in range(1, n_harmonics + 1):
        features.append(np.sin(i * x_rad[:, 0]))
        features.append(np.cos(i * x_rad[:, 0]))
    
    return np.column_stack(features)

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
# Data
x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 
              190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]).reshape(-1, 1)
y = np.array([8.71, 8.56, 8.18, 7.58, 6.70, 5.52, 4.15, 2.75, 1.37, 0.00, 1.63, 3.05, 4.30, 5.65, 
              6.66, 7.54, 8.14, 8.53, 8.66, 8.55, 8.17, 7.59, 6.82, 5.76, 4.17, 2.76, 1.27, 0.00, 
              1.76, 3.17, 4.56, 5.72, 6.76, 7.59, 8.19, 8.59, 8.71])
y1 = np.array([8.71, 8.58, 8.18, 7.54, 6.67, 5.60, 4.36, 2.98, 1.51, 0.00, 1.51, 2.98, 4.36, 5.60, 
               6.67, 7.54, 8.18, 8.58, 8.71, 8.58, 8.18, 7.54, 6.67, 5.60, 4.36, 2.98, 1.51, 0.00, 
               1.51, 2.98, 4.36, 5.60, 6.67, 7.54, 8.18, 8.58, 8.71])

# Create Fourier features
n_harmonics = 8  # Number of harmonics to use
X_fourier = create_fourier_features(x, n_harmonics)

# Fit models
model = LinearRegression()
model1 = LinearRegression()
model.fit(X_fourier, y)
model1.fit(X_fourier, y1)

# Generate smooth predictions
x_smooth = np.linspace(0, 360, 200)
X_fourier_smooth = create_fourier_features(x_smooth, n_harmonics)
y_pred = model.predict(X_fourier_smooth)
y1_pred = model1.predict(X_fourier_smooth)

# Create plot
plt.figure(figsize=(12, 8))

# Plot original data points
plt.scatter(x, y, color='blue', label='Data $U$', alpha=0.5)
plt.scatter(x, y1, color='red', label='Theoretical $U$', alpha=0.5)

# Plot regression lines
plt.plot(x_smooth, y_pred, color='blue', linestyle='-', label='Fourier Fit Data $U$')
plt.plot(x_smooth, y1_pred, color='red', linestyle='-', label='Fourier Fit Theoretical $U$')

# Add Pred std
plt.fill_between(x_smooth, y_pred - 0.1, y_pred + 0.1, color='pink', alpha=0.5, label='Pred Std')

# Customize plot
plt.xlabel('$\\theta(\mathrm{degree})$')
plt.ylabel('$U(\mathrm{mV})$')
plt.title('Fourier Series Regression of $U$ vs $\\theta$')
plt.grid(True, alpha=0.3)
plt.legend()


plt.savefig("plot10.pdf")

# Print model scores
print(f"R² score for y: {model.score(X_fourier, y):.4f}")
print(f"R² score for y1: {model1.score(X_fourier, y1):.4f}")

# Print Fourier coefficients
print("\nFourier coefficients for y:")
terms = ['Constant'] + [f'sin({i}x)' for i in range(1, n_harmonics + 1)] + [f'cos({i}x)' for i in range(1, n_harmonics + 1)]
for term, coef in zip(terms, model.coef_):
    print(f"{term}: {coef:.4f}")