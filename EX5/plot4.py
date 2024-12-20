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

# Data Preparation
a_values = np.array([10, 15, 20, 25, 30])
e_k_values = np.array([0.232, 0.212, 0.180, 0.145, 0.100])
e_p_values = np.array([0.017, 0.039, 0.070, 0.109, 0.157])
e_values = np.array([0.249, 0.251, 0.249, 0.254, 0.257])

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(a_values, e_k_values, marker='o', label='$E_k$ (J)', color='blue', alpha=0.7)
plt.plot(a_values, e_p_values, marker='o', label='$E_p$ (J)', color='orange', alpha=0.7)
plt.plot(a_values, e_values, marker='o', label='$E$ (J)', color='green', alpha=0.7)

# Customize the plot
plt.xlabel('$A$ (cm)')
plt.ylabel('Energy (J)')
plt.grid(True)
plt.legend()

plt.savefig("plot4.pdf")


