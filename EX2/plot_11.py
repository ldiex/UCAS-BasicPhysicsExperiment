import numpy as np
import matplotlib.pyplot as plt
import matplotlib

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})

plt.figure(figsize=(8, 4))

matplotlib.rcParams['mathtext.fontset'] = 'stix'
# Data
y = np.array([0.212, 0.213, 0.212, 0.212, 0.212, 0.212, 0.212, 0.212, 0.212, 0.212, 0.212])
x = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]).reshape(-1, 1)
x = x * 1e-3
plt.scatter(x, y, color='blue', label='Data Points')
plt.ylim(0.20, 0.22)
plt.title('$B$ vs $f$')
plt.ylabel('$B(\mathrm{mT})$')
plt.xlabel('$f(\mathrm{Hz})$')
plt.legend()
plt.grid()

# Restrict the height of the plot

plt.savefig("plot11.pdf")

