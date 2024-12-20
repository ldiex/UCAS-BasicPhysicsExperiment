import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['font.family'] = 'STIX Two Text'
# Data for theta, U+ and U-

Phi = [30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0, 44.0, 46.0,
       48.0, 50.0, 52.0, 54.0, 56.0, 58.0, 60.0, 62.0, 64.0,
       66.0, 68.0, 70.0]

U = [0,0,0,0,0,0.1,0,0.1,0.3,
     0.2,0.5,2,4.7,4.7,4,2.6,0.1,0.3,
     0,0,0]


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
plt.savefig('布拉格衍射-(110)面-粗扫数据.pdf')
plt.show()
