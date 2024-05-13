import numpy as np
import matplotlib.pyplot as plt

strain_x = np.genfromtxt('src/data/final_output/pristine/strain-x/1/stress_strain.dat')
strain_y = np.genfromtxt('src/data/final_output/pristine/strain-y/1/stress_strain.dat')

# Criar figura com dois graficos
fig, axs = plt.subplots(2, figsize=(12, 8))

# Deformacao em x de arquivo strain-x
axs[0].plot(strain_x[:, 0], strain_x[:, 1], label='Ex. Strain in x-axis (strain-x)')
axs[0].set_xlabel('Strain')
axs[0].set_ylabel('Stress')
axs[0].legend()

# Deformacao em y de arquivo strain-y
axs[1].plot(strain_y [:, 0], strain_y [:, 2], label='Ex. Strain in y-axis (strain-y)')
axs[1].set_xlabel('Strain')
axs[1].set_ylabel('Stress')
axs[1].legend()

# Ajusatar layout e plotar
plt.tight_layout()
plt.show()
