import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)                # Sine wave

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the line plot
ax.plot(x, y)

# Add title and labels
ax.set_title('Simple Line Plot', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

plt.tight_layout()
plt.show()
