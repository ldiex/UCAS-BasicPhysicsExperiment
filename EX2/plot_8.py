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
y = np.array([0.213, 0.213, 0.213, 0.213, 0.213, 0.213, 0.213, 0.214, 0.214, 0.213, 0.213])
x = np.array([-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25]).reshape(-1, 1)
x = x * 1e-3
plt.scatter(x, y, color='blue', label='Data Points')
plt.ylim(0.20, 0.22)
plt.title('$B$ vs $X$')
plt.ylabel('$B(\mathrm{mT})$')
plt.xlabel('$X(\mathrm{mm})$')
plt.legend()
plt.grid()

# Restrict the height of the plot

plt.savefig("plot8.pdf")

