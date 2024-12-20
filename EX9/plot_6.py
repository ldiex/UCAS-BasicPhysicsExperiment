import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['font.family'] = 'STIX Two Text'
# Data for theta, U+ and U-

Phi = [64,65,66,67,68,69,70,71,72]

U = [9.9,28.2,59.4,81,98.1,83.9,30.6,2.6,1]


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
plt.savefig('布拉格衍射-(100)面-极大.pdf')
plt.show()
