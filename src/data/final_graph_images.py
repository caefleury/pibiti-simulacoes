import numpy as np
import matplotlib.pyplot as plt
import mplcursors

gold_substrate = False
strain = 'strain-x'
base_path = 'pristine/{strain}/{i}/stress_strain.dat'

fig, ax = plt.subplots(figsize=(18, 10))

def moving_average(x, window_size):
    return np.convolve(x, np.ones(window_size), 'valid') / window_size

window_size = 30
colors = ['b', 'g', 'r', 'c', 'm']


# Load all data first
all_data = []
for i in range(1, 6):
    simulation_data = base_path.format(strain=strain, i=i)
    strain_gold = np.genfromtxt(f'src/data/gold_substrate_final_simulation/{simulation_data}')
    all_data.append(strain_gold)

# Find the minimum length across all simulations
min_length = 1755

# Trim all datasets to the minimum length
trimmed_data = [data[:min_length] for data in all_data]


max_height = 90  # Initialize max_height variable

for i, strain_gold in enumerate(trimmed_data):
    if gold_substrate:
        if strain == 'strain-x':
            smoothed_stress_gold = moving_average(strain_gold[:, 1], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0], smoothed_stress_gold, color=colors[i], linewidth=3.2)
        elif strain == 'strain-y':
            smoothed_stress_gold = moving_average(strain_gold[:, 2], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, color=colors[i], linewidth=3.2)
    else:
        if strain == 'strain-x':
            smoothed_stress_gold = moving_average(strain_gold[:, 1], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, color=colors[i], linewidth=3.2)
        elif strain == 'strain-y':
            smoothed_stress_gold = moving_average(strain_gold[:, 2], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, color=colors[i], linewidth=3.2)

# Make the graph borders darker/bolder
for spine in ax.spines.values():
    spine.set_linewidth(2)  # Increase this value for thicker borders
    spine.set_color('black')  # Change to your preferred color

plt.yticks(np.arange(15, 90, 15))
plt.xticks(np.arange(0.05, 2, 0.05))

# plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x * 100:.0f}')) # %

# Add axis labels
# ax.set_xlabel('Strain (%)', fontsize=14)
# ax.set_ylabel('Stress (GPa)', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=10)

if strain == 'strain-x': 
    if base_path[0:8] == 'pristine':
        letter = '(a)'
        # plt.gca().xaxis.set_ticks([])
    if base_path[0:12] == 'center_crack':
        letter = '(b)'
        # plt.gca().xaxis.set_ticks([])
        # plt.gca().yaxis.set_ticks([])
    if base_path[0:12] == 'x_axis_crack':
        letter = '(c)'
        # plt.gca().xaxis.set_ticks([])
        # plt.gca().yaxis.set_ticks([])
    if base_path[0:12] == 'y_axis_crack':
        letter = '(d)'
        # plt.gca().xaxis.set_ticks([])
        # plt.gca().yaxis.set_ticks([])
else: 
    if base_path[0:8] == 'pristine':
        letter = '(e)'
    if base_path[0:12] == 'center_crack':
        letter = '(f)'
        # plt.gca().yaxis.set_ticks([])
    if base_path[0:12] == 'x_axis_crack':
        letter = '(g)'
        # plt.gca().yaxis.set_ticks([])
    if base_path[0:12] == 'y_axis_crack':
        letter = '(h)'
        # plt.gca().yaxis.set_ticks([])


cursor = mplcursors.cursor(hover=True)
@cursor.connect("add")
def on_add(sel):
    x, y = sel.target
    sel.annotation.set_text(f"Strain={x*100:.2f}, Stress={y:.2f}")

plt.gca().xaxis.set_ticks([])
plt.gca().yaxis.set_ticks([])

# Set the y-axis limit
ax.set_ylim(bottom=0, top=max_height)
ax.set_xlim(left=0.000, right=0.20)

# Add a letter annotation in the upper right corner
ax.text(0.95, 0.95, letter, transform=ax.transAxes, fontsize=60,
        verticalalignment='top', horizontalalignment='right')


plt.margins(0)
plt.tight_layout()
plt.get_current_fig_manager().toolbar.pan()
plt.get_current_fig_manager().toolbar.zoom()

plt.show()
