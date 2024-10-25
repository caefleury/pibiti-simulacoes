import numpy as np
import matplotlib.pyplot as plt
import mplcursors

melting_folder = True
base_path = 'melting/{i}/energias_termo_aquec.dat'

fig, ax = plt.subplots(figsize=(15, 15))

def moving_average(x, window_size):
    return np.convolve(x, np.ones(window_size), 'valid') / window_size

window_size = 200
colors = ['b', 'g', 'r', 'c', 'm']

# Load all data first
all_data = []
for i in range(1, 6):
    simulation_data = base_path.format(i=i)
    if melting_folder:
        melting = np.genfromtxt(f'src/data/no_gold_final_simulation/pristine/{simulation_data}')
    all_data.append(melting)

for i, melting_data in enumerate(all_data):
    smoothed_temp = moving_average(melting_data[:, 2], window_size)
    smoothed_energy = moving_average(melting_data[:, 4], window_size)
    ax.plot(smoothed_temp, melting_data[:len(smoothed_energy), 4], color=colors[i], linewidth=2.5)


# Make the graph borders darker/bolder
for spine in ax.spines.values():
    spine.set_linewidth(2)  # Increase this value for thicker borders
    spine.set_color('black')  # Change to your preferred color

# plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x * 0.001:.0f}'))
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y * 0.00001:.1f}'))

ax.set_ylabel('Energy (ev/atom)')
ax.set_xlabel('Temperature (K)')

# plt.gca().xaxis.set_ticks([])
# plt.gca().yaxis.set_ticks([])

ax.set_title('Pristine Melting')

plt.margins(0)

plt.tight_layout()
plt.subplots_adjust(bottom=0.05)
plt.get_current_fig_manager().toolbar.pan()
plt.get_current_fig_manager().toolbar.zoom()

plt.show()
