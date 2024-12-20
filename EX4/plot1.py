import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
matplotlib.rcParams['mathtext.fontset'] = 'stix'

data = pd.read_excel('Cu-data.xlsx')

# x is the first column of the data
x = data.iloc[:, 0]

# We have a series of y, each column from the third to the last is a y
y = data.iloc[:, 2:]



# plot all ys in the same figure, with different colors
fig, ax = plt.subplots()
for i in range(y.shape[1]):
    ax.plot(x, y.iloc[:, i], label=f'$n = {i+1}$')

# Set the Size of the figure
fig.set_size_inches(10, 6)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Signal Voltage (mV)')
ax.legend()
plt.savefig('Cu-data.pdf')
print(data.head())
