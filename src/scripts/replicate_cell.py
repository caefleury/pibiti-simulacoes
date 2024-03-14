

import sys
sys.path.append('./src/utils')
from utils import read_xyz, write_xyz

# Replicar a célula unitária


def replicate_cell(atoms, lattice_constants, n_replications_x, n_replications_y):
    replicated_atoms = []
    for i in range(n_replications_x):
        for j in range(n_replications_y):
            for index, (atom, position) in enumerate(atoms):
                new_position = [
                    position[0] + (lattice_constants[0]) * i, position[1] + (lattice_constants[1])*j, 0.0]
                replicated_atoms.append((atom, new_position))
    return replicated_atoms


# Vetores de rede (lattice constants)
a = 6.3028
b = 4.9302
lattice_constants = [a, b]

# Parâmetros
unit_cell_file = 'src/simulations/unit_cell.xyz'
n_replications_x = 15
n_replications_y = 15

if (__name__ == '__main__'):
    # Ler a célula unitária
    n_atoms, comment, atoms = read_xyz(unit_cell_file)

    # Replicar a célula unitária
    replicated_atoms = replicate_cell(
        atoms, lattice_constants, n_replications_x, n_replications_y)

    # Escreva o arquivo .xyz com a estrutura replicada
    OUTPUT_STRUCTURE_FILE = 'src/simulations/structure.xyz'

    write_xyz(OUTPUT_STRUCTURE_FILE, n_replications_x *
            n_replications_y * n_atoms, comment, replicated_atoms)

    print('Estrutura replicada com sucesso! arquivo salvo em {}'.format(
        OUTPUT_STRUCTURE_FILE))
