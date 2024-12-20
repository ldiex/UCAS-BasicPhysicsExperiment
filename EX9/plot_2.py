import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['font.family'] = 'STIX Two Text'
# Data for theta, U+ and U-
theta = [18,19,20,21,22,23,24,25,26]
U_plus = [13.1,16.6,20.2,21.8,20.9,16.6,12.6,8.9,4.6]
U_minus = [12,18.2,23,25.2,26.7,24.8,20,15,9.6]
theta = np.array(theta)
# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(theta, U_plus, label='$U+$', marker='o')


plt.plot(theta, U_minus, label='$U-$', marker='x')

# Adding labels and title
plt.xlabel(r'$\theta$ (degrees)')
plt.ylabel('Voltage (mV)')
plt.title(r'$U_{\theta+}$ and $U_{\theta-}$ vs $\theta$')

# Adding legend
plt.legend()

# Show the plot
plt.grid(True)
plt.savefig('双缝干涉-一级极大.pdf')
plt.show()
