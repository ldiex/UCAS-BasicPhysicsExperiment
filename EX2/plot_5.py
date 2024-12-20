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
y = np.array([-68.2, -135.2, -150.1, -150.5, -150.6, -150.6, -150.5, -150.4, -150.4, -150.5, -150.5, -150.4, -150.4, -150.3, -150.3, -150.4])
x = np.array([44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14]).reshape(-1, 1)
x = x * 1e-3
plt.scatter(x, y, color='blue', label='Data Points')
plt.title('$B$ vs $X$')
plt.ylabel('$B(\mathrm{mT})$')
plt.xlabel('$X(\mathrm{mm})$')
plt.legend()
plt.grid()

# Restrict the height of the plot

plt.savefig("plot5.pdf")

