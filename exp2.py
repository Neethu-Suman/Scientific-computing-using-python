
# Plot sinewaves of frequency 50 and 100 Hz on the same figure window.

import numpy as np
import matplotlib.pyplot as plt

# Define the time axis
t = np.linspace(0, 0.1, 1000)  # Plots 0 to 0.1 seconds

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
# Plot sinewaves of frequency 50 and 100 Hz on the same figure window.

