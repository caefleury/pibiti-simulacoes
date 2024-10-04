import numpy as np
import matplotlib.pyplot as plt
import mplcursors

gold_substrate = True
strain = 'strain-x'
base_path = 'center_crack/{strain}/{i}/stress_strain.dat'

# Criar figura para um gráfico
fig, ax = plt.subplots(figsize=(18, 10))

def moving_average(x, window_size):
    return np.convolve(x, np.ones(window_size), 'valid') / window_size

window_size = 10
colors = ['b', 'g', 'r', 'c', 'm']  # Cores para as 5 simulações

for i in range(1, 6):
    # Caminho para cada simulação
    simulation_data = base_path.format(strain=strain, i=i)
    
    # Carregar dados das simulações com substrato de ouro
    strain_gold = np.genfromtxt(f'src/data/gold_substrate_final_simulation/{simulation_data}')
    
    if gold_substrate:
        if strain == 'strain-x':
            # Deformacao em x de simulação com o substrato de ouro
            smoothed_stress_gold = moving_average(strain_gold[:, 1], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, label=f'Simulation {i} with gold', color=colors[i-1])
            
        elif strain == 'strain-y':
            # Deformacao em y de simulação com o substrato de ouro
            smoothed_stress_gold = moving_average(strain_gold[:, 2], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, label=f'Simulation {i} with gold', color=colors[i-1])
    else:
        if strain == 'strain-x':
            # Deformacao em x de simulação com o substrato de ouro
            smoothed_stress_gold = moving_average(strain_gold[:, 1], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, label=f'Simulation {i} without gold', color=colors[i-1])
            
        elif strain == 'strain-y':
            # Deformacao em y de simulação com o substrato de ouro
            smoothed_stress_gold = moving_average(strain_gold[:, 2], window_size)
            ax.plot(strain_gold[:len(smoothed_stress_gold), 0],
                    smoothed_stress_gold, label=f'Simulation {i} without gold', color=colors[i-1])

# Configurar o gráfico
ax.set_xlabel('Strain (x)')
ax.set_ylabel('Stress (y)')
ax.legend()

# Adicionando tooltips interativos
cursor = mplcursors.cursor(hover=True)

@cursor.connect("add")
def on_add(sel):
    x, y = sel.target
    sel.annotation.set(text=f'Strain(x): {x:.4f}\nStress(y): {y:.4f}')

# Ajustar layout e plotar
plt.tight_layout()

# Ativar a barra de ferramentas de navegação
plt.get_current_fig_manager().toolbar.pan()
plt.get_current_fig_manager().toolbar.zoom()

plt.show()
