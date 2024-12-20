import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['font.family'] = 'STIX Two Text'
# Data for theta, U+ and U-
theta = [0, 2, 4, 6, 8, 10, 12, 14, 16, 
         18, 20, 22, 24, 26, 28, 30, 32, 34,
         36, 38, 40, 42, 44, 46, 48, 50]
U_plus = [23, 21.2, 15.1, 7.2, 0.5, 0, 0.1, 1.3, 4.7, 
          12.4, 19.5, 20.8, 13.2, 5.4, 1.4, 0.4, 0.2, 0.3, 
          0.7, 1.3, 0.9, 0.5, 0.9, 3, 2.8, 1.2]
U_minus = [23, 21.5, 18.6, 13.2, 6, 1.2, 0.8, 1.9, 4.2, 
           13, 23, 26.1, 20, 9.8, 2.5, 1.1, 1.1, 1.5, 
           2.6, 3.4, 1.9, 0.4, 0.5, 2.8, 5.5, 2.5]
theta = np.array(theta)
# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(theta, U_plus, label='$U+$', marker='o')


plt.plot(-theta, U_minus, label='$U-$', marker='x')

# Adding labels and title
plt.xlabel(r'$\theta$ (degrees)')
plt.ylabel('Voltage (mV)')
plt.title(r'$U_{\theta+}$ and $U_{\theta-}$ vs $\theta$')

# Adding legend
plt.legend()

# Show the plot
plt.grid(True)
plt.savefig('双缝干涉-粗扫数据.pdf')
plt.show()
