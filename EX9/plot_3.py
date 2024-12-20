import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['font.family'] = 'STIX Two Text'
# Data for theta, U+ and U-
theta_plus = [7,8,9,10,11,12,13,14,15]
U_plus = [2.3,0.5,0.1,0,0,0.2,0.6,1.1,2.5]
theta_minus = [7,8,9,10,11,12,13,14,15]
U_minus = [10,6.4,2.6,1.1,0.7,0.8,1.2,1.9,3]

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
plt.savefig('双缝干涉-零级极小.pdf')
plt.show()
