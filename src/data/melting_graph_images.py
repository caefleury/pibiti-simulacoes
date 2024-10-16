import numpy as np
import matplotlib.pyplot as plt
import mplcursors

melting_folder = True
base_path = 'melting/{i}/energias_termo_aquec.dat'

fig, ax = plt.subplots(figsize=(15, 15))

def moving_average(x, window_size):
    return np.convolve(x, np.ones(window_size), 'valid') / window_size

window_size = 90
colors = ['b', 'g', 'r', 'c', 'm']

# Load all data first
all_data = []
for i in range(1, 6):
    simulation_data = base_path.format(i=i)
    if melting_folder:
        melting = np.genfromtxt(f'src/data/no_gold_final_simulation/pristine/{simulation_data}')
    all_data.append(melting)

for i, melting_data in enumerate(all_data):
    smoothed_stress = moving_average(melting_data[:, 4], window_size)
    ax.plot(melting_data[:len(smoothed_stress), 0],
            smoothed_stress, color=colors[i], linewidth=2.5)


# Make the graph borders darker/bolder
for spine in ax.spines.values():
    spine.set_linewidth(2)  # Increase this value for thicker borders
    spine.set_color('black')  # Change to your preferred color

ax.set_xlabel('x')
ax.set_ylabel('y')


plt.margins(0)
plt.tight_layout()
plt.get_current_fig_manager().toolbar.pan()
plt.get_current_fig_manager().toolbar.zoom()

plt.show()
