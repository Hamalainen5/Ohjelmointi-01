from matplotlib import pyplot as plt, patches
import numpy as np

# Create a wider figure (three times the default width of 6.4)
fig = plt.figure(figsize=(6.4 * 3, 4.8))
ax = fig.subplots()

# Draw the unit circle
ymp = patches.Circle((0, 0), radius=1, fill=False, edgecolor='blue', linestyle='--', linewidth=2)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to center
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks on the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Set equal scaling and adjust x-axis range
ax.axis('equal')
ax.set_xlim(-3 * np.pi, 3 * np.pi)
ax.set_ylim(-1.5, 1.5)

# Define angles in degrees and convert to radians
angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]
angles_rad = np.radians(angles_deg)

# Calculate (x, y) positions on the unit circle for each angle
x = np.cos(angles_rad)
y = np.sin(angles_rad)

# Define colors, labels, and line styles for each angle
colors = ['red', 'green', 'blue', 'purple', 'orange', 'brown', 'cyan', 'magenta']
styles = ['--', '-.', ':', '--', '-.', ':', '--', '-.']
labels = [r'30°', r'45°', r'60°', r'90°', r'120°', r'150°', r'180°', r'270°']

# Plot points on the unit circle with unique styles and add annotations
for i in range(len(angles_rad)):
    ax.plot([0, x[i]], [0, y[i]], color=colors[i], linestyle=styles[i], label=labels[i], marker='X')
    ax.annotate(labels[i],
                xy=(x[i], y[i]), xycoords='data',
                xytext=(+10, +10), textcoords='offset points', fontsize=12,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

# Set axis ticks and labels for -3π to 3π range
xticks = np.arange(-3 * np.pi, 3.1 * np.pi, np.pi)
ax.set_xticks(xticks)
ax.set_xticklabels([f"{(np.round(val / np.pi))}π" for val in xticks])

plt.yticks([-1, 0, 1], labels=['-1', '0', '1'])

# Add a legend
ax.legend(loc='upper right', fontsize=10)

# Display the plot
plt.show()
