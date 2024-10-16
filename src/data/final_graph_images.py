import numpy as np
import matplotlib.pyplot as plt
import mplcursors

gold_substrate = True
strain = 'strain-x'
base_path = 'pristine/{strain}/{i}/stress_strain.dat'

fig, ax = plt.subplots(figsize=(15, 15))

def moving_average(x, window_size):
    return np.convolve(x, np.ones(window_size), 'valid') / window_size

window_size = 60
colors = ['b', 'g', 'r', 'c', 'm']

# Load all data first
all_data = []
for i in range(1, 6):
    simulation_data = base_path.format(strain=strain, i=i)
    strain_gold = np.genfromtxt(f'src/data/gold_substrate_final_simulation/{simulation_data}')
    all_data.append(strain_gold)

# Find the minimum length across all simulations
min_length = 2000
# Trim all datasets to the minimum length
trimmed_data = [data[:min_length] for data in all_data]

max_height = 90  # Initialize max_height variable

for i, strain_gold in enumerate(trimmed_data):
    if gold_substrate:
        if strain == 'strain-x':
            smoothed_stress_gold = moving_average(strain_gold[:, 1], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, color=colors[i], linewidth=2.5)
        elif strain == 'strain-y':
            smoothed_stress_gold = moving_average(strain_gold[:, 2], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, color=colors[i], linewidth=2.5)
    else:
        if strain == 'strain-x':
            smoothed_stress_gold = moving_average(strain_gold[:, 1], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, color=colors[i], linewidth=2.5)
        elif strain == 'strain-y':
            smoothed_stress_gold = moving_average(strain_gold[:, 2], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, color=colors[i], linewidth=2.5)

# Make the graph borders darker/bolder
for spine in ax.spines.values():
    spine.set_linewidth(2)  # Increase this value for thicker borders
    spine.set_color('black')  # Change to your preferred color


# Set the y-axis limit
ax.set_ylim(bottom=0, top=max_height ) 

plt.margins(0)
plt.tight_layout()
plt.get_current_fig_manager().toolbar.pan()
plt.get_current_fig_manager().toolbar.zoom()

plt.show()
