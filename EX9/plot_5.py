import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['font.family'] = 'STIX Two Text'
# Data for theta, U+ and U-

Phi = [30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0, 44.0, 46.0,
       48.0, 50.0, 52.0, 54.0, 56.0, 58.0, 60.0, 62.0, 64.0,
       66.0, 68.0, 70.0, 72.0, 74.0, 76.0, 78.0, 80.0]

U = [1.8, 2.1, 1.8, 2.2, 4.8, 9.2, 5.7, 1.2, 0.8,
     5.0, 6.3, 1.2, 0.8, 2.0, 1.1, 13.0, 26.3, 9.0,
     57.2, 97.2, 30.7, 1.1, 2.6, 15.2, 0.2, 11.0]


# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(Phi, U, label='$U$', marker='o')



# Adding labels and title
plt.xlabel(r'$\Phi$ (degrees)')
plt.ylabel('Voltage (mV)')
plt.title(r'$U$ vs $\Phi$')

# Adding legend
plt.legend()

# Show the plot
plt.grid(True)
plt.savefig('布拉格衍射-(100)面-粗扫数据.pdf')
plt.show()
