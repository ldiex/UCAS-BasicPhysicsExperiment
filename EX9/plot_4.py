import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['font.family'] = 'STIX Two Text'
# Data for theta, U+ and U-
theta_plus = [28,29,30,31,32,33,34,35,36]
U_plus = [1.3,0.6,0.4,0.3,0.2,0.2,0.3,0.5,0.8]
theta_minus = [27,28,29,30,31,32,33,34,35]
U_minus = [5.2,2.4,1.4,1.1,1,1.1,1.2,1.5,1.9]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(theta_plus, U_plus, label='$U+$', marker='o')


plt.plot(theta_minus, U_minus, label='$U-$', marker='x')

# Adding labels and title
plt.xlabel(r'$\theta$ (degrees)')
plt.ylabel('Voltage (mV)')
plt.title(r'$U_{\theta+}$ and $U_{\theta-}$ vs $\theta$')

# Adding legend
plt.legend()

# Show the plot
plt.grid(True)
plt.savefig('双缝干涉-一级极小.pdf')
plt.show()
