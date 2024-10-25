import numpy as np
import matplotlib.pyplot as plt
import mplcursors


strain = 'strain-x'
simulation_number = 1

simulation_data = f'pristine/{strain}/{simulation_number}/stress_strain.dat'
strain_no_gold = np.genfromtxt(
    f'src/data/no_gold_final_simulation/{simulation_data}')
strain_gold = np.genfromtxt(
    f'src/data/gold_substrate_final_simulation/{simulation_data}')

# Criar figura com dois graficos
fig, axs = plt.subplots(2, figsize=(18, 10))

# Media móvel
def moving_average(x, window_size):
    return np.convolve(x, np.ones(window_size), 'valid') / window_size

window_size = 30

if strain == 'strain-x':
    # Deformacao em x de simulação sem o substrato de ouro
    smoothed_stress_no_gold = moving_average(strain_no_gold[:, 1], window_size)
    line1, = axs[0].plot(strain_no_gold[:len(smoothed_stress_no_gold), 0],
                         smoothed_stress_no_gold, label='Ex. strain-x simulation without gold substrate')
    axs[0].set_xlabel('Strain (x)')
    axs[0].set_ylabel('Stress (y)')
    axs[0].legend()

    # Deformacao em x de simulação com o substrato de ouro
    smoothed_stress_gold = moving_average(strain_gold[:, 1], window_size)
    line2, = axs[1].plot(strain_gold[:len(smoothed_stress_gold), 0],
                         smoothed_stress_gold, label='Ex. strain-x simulation with gold substrate')
    axs[1].set_xlabel('Strain (x)')
    axs[1].set_ylabel('Stress (y)')
    axs[1].legend()

elif strain == 'strain-y':
    # Deformacao em y de simulação sem o substrato de ouro
    smoothed_stress_no_gold = moving_average(strain_no_gold[:, 2], window_size)
    line1, = axs[0].plot(strain_no_gold[:len(smoothed_stress_no_gold), 0],
                         smoothed_stress_no_gold, label='Ex. strain-y simulation without gold substrate')
    axs[0].set_xlabel('Strain (x)')
    axs[0].set_ylabel('Stress (y)')
    axs[0].legend()

    # Deformacao em y de simulação com o substrato de ouro
    smoothed_stress_gold = moving_average(strain_gold[:, 2], window_size)
    line2, = axs[1].plot(strain_gold[:len(smoothed_stress_gold), 0],
                         smoothed_stress_gold, label='Ex. strain-y simulation with gold substrate')
    axs[1].set_xlabel('Strain (x)')
    axs[1].set_ylabel('Stress (y)')
    axs[1].legend()

# Adicionando tooltips interativos
cursor1 = mplcursors.cursor(line1, hover=True)
cursor2 = mplcursors.cursor(line2, hover=True)

@cursor1.connect("add")
def on_add1(sel):
    x, y = sel.target
    sel.annotation.set(text=f'Strain(x): {x:.4f}\nStress(y): {y:.4f}')


@cursor2.connect("add")
def on_add2(sel):
    x, y = sel.target
    sel.annotation.set(text=f'Strain(x): {x:.4f}\nStress(y): {y:.4f}')


# Ajustar layout e plotar
plt.tight_layout()

# Ativar a barra de ferramentas de navegação
plt.get_current_fig_manager().toolbar.pan()
plt.get_current_fig_manager().toolbar.zoom()

plt.show()
