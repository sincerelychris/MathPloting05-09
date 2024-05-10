import matplotlib.pyplot as plt
import numpy as np

# Define the line equation
x = np.linspace(-10, 10, 100)
y = -x

# Create the plot
plt.figure(figsize=(6, 6))
plt.plot(x, y, label='y = -x', color='blue')
plt.title('Graph of $y = -x$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
