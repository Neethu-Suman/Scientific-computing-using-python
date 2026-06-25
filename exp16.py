# Write a Python program to generate and plot two sine waves of frequencies 50 Hz and 100 Hz on the same graph using NumPy and Matplotlib.
import numpy as np
import matplotlib.pyplot as plt
# Define the time axis
t = np.linspace(0, 20, 1000)
# Define the frequencies
f1 = 50
f2 = 100
# Generate the sine waves
s1 = np.sin(2 * np.pi * f1 * t)
s2 = np.sin(2 * np.pi * f2 * t)
# Create the plot
plt.plot(t, s1, label='50 Hz')
plt.plot(t, s2, label='100 Hz')

# Add labels and legend
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
# Show the plot
plt.show()
