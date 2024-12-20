import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.interpolate import make_interp_spline

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
matplotlib.rcParams['mathtext.fontset'] = 'stix'
plt.style.use('seaborn-v0_8-paper')

I1 = [600.1, 550.9, 499.3, 449.7, 400.3, 349.3, 300.5, 250.2, 199.5, 149.9, 100.1, 50.6, 0, -50.4, -100.3, -150.1, -200.7, -250.7, -299.9, -349.8, -400.1, -459.3, -500.0, -550.3, -600]
I2 = [-600, -550.3, -500.6, -450.3,  -399.2, -349.5, -299.9, -249.7, -200.3, -149.6, -100.1, -49.7, 0, 50.6, 100.5, 150.5, 200.2, 249.8, 301.6, 350.4, 400.8, 450.3, 500.0, 550.4, 600.4]

H1 = [2877.7, 2496.4, 2116.6, 1761.9, 1421.5, 1088.8, 794.2, 521.5, 278.5, 65.7, -127.8, -322.5, -498.5, -672.1, -839.0, -1003.8, -1172.8, -1348.8, -1527.7, -1715.0, -1912.0, -2195.2, -2340.2, -2581.8, -2838.7]
H2 = [-2838.7, -2467.2, -2101.4, -1739.5, -1384.3, -1055.5, -750.4, -470.2, -225.9, -2.1, 199.1, 391.2, 571.0, 746.3, 915.8, 1081.6, 1248.2, 1422.8, 1610.0, 1793.8, 1989.7, 2196.0, 2417.9, 2662.8, 2926.7]

B1 = [333.5, 329.0, 321.1, 311.9, 300.7, 286.2, 268.6, 245.6, 217.4, 185.9, 151.1, 116.9, 78.3, 39.6, 0.5, -38.8, -78.5, -116.3, -152.6, -188.5, -223.4, -256.4, -286.9, -314.8, -339.5]
B2 = [-339.5, -332.8, -325.2, -316.2, -305.1, -291.7, -274.7, -253.0, -226.7, -195.5, -162.3, -126.5, -89.7, -51.0, -12.3, 27.1, 66.0, 103.5, 141.9, 176.9, 212.1, 244.5, 274.7, 302.2, 326.2]


# Sort the data
sorted_indices = np.argsort(H1)
H1 = np.array(H1)[sorted_indices]
B1 = np.array(B1)[sorted_indices]

sorted_indices = np.argsort(H2)
H2 = np.array(H2)[sorted_indices]
B2 = np.array(B2)[sorted_indices]

# Create the scatter plot
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.scatter(H1, B1, color='blue')
plt.scatter(H2, B2, color='orange')

# Create smooth curves
H1_new = np.linspace(min(H1), max(H1), 300)
spl_B1 = make_interp_spline(H1, B1, k=1)
B1_smooth = spl_B1(H1_new)

H2_new = np.linspace(min(H2), max(H2), 300)
spl_B2 = make_interp_spline(H2, B2, k=1)
B2_smooth = spl_B2(H2_new)


# Plot smooth curves
plt.plot(H1_new, B1_smooth, color='blue')
plt.plot(H2_new, B2_smooth, color='orange')

# Add labels and title
plt.xlabel('$H$ (A/m)')
plt.ylabel('$B$ (mT)')

plt.title('The Hysteresis Loop of a Mold Steel Sample')


# Add a grid for better readability
plt.grid(True)

# Show Plot
plt.savefig('plot6.pdf')
