

from my_utils import read_xyz, write_xyz
import sys
sys.path.append('./src/utils')

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

def run():
    # Parâmetros
    unit_cell_file = 'src/simulations/unit_cell.xyz'
    n_replications_x = 17
    n_replications_y = 21

    # Ler a célula unitária
    n_atoms, comment, atoms = read_xyz(unit_cell_file)

    # Vetores de rede (lattice constants)
    a = float(comment.split()[2])
    b = float(comment.split()[-2])
    lattice_constants = [a, b]

    # Replicar a célula unitária
    replicated_atoms = replicate_cell(
        atoms, lattice_constants, n_replications_x, n_replications_y)

    # Escreva o arquivo .xyz com a estrutura replicada
    OUTPUT_STRUCTURE_FILE = 'src/simulations/pristine_structure.xyz'

    write_xyz(OUTPUT_STRUCTURE_FILE, n_replications_x *
            n_replications_y * n_atoms, comment, replicated_atoms)

    print('Estrutura "pristine" replicada com sucesso! arquivo salvo em {}'.format(
        OUTPUT_STRUCTURE_FILE))
