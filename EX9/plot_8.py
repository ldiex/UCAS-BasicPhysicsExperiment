import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['font.family'] = 'STIX Two Text'
# Data for theta, U+ and U-

Phi = [51,52,53,54,55,56,57,58,59]

U = [1.3,1.9,2.9,4.7,6.1,4.7,4.2,4,3.1]


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
plt.savefig('布拉格衍射-(110)面-极大.pdf')
plt.show()
