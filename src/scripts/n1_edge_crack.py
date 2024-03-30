

from my_utils import read_xyz, write_xyz
from n1_crack_utils import edge_center_crack


# Replicar a célula unitária com os nanocracks lineares (n2)
def replicate_edge_crack(atoms, lattice_constants,
                         n_replications_x, n_replications_y, crack_size):
    replicated_atoms = []
    for x in range(n_replications_x):
        for y in range(n_replications_y):
            for index, (atom, position) in enumerate(atoms):
                # POSICOES PERMANECEM CONSTANTES
                new_position = [
                    position[0] + (lattice_constants[0]) * x, position[1] + (lattice_constants[1]) * y, 0.0]

                if x == (n_replications_x // 2):
                    if edge_center_crack(
                            y, atom, n_replications_y, crack_size, index, new_position):
                        atom, new_position = edge_center_crack(
                            y, atom, n_replications_y, crack_size, index, new_position)
                        replicated_atoms.append((atom, new_position))

                else:
                    replicated_atoms.append((atom, new_position))

    return [len(replicated_atoms), replicated_atoms]


def run():
    # Parâmetros
    INPUT_UNIT_CELL_FILE = 'src/simulations/unit_cell.xyz'
    OUTPUT_STRUCTURE_FILE = 'src/simulations/n1_edge_crack_structure.xyz'
    n_replications_x = 17
    n_replications_y = 21
    crack_size = 9

    # Ler a célula unitária
    n_atoms, comment, atoms = read_xyz(INPUT_UNIT_CELL_FILE)

    # Vetores de rede (lattice constants)
    a = float(comment.split()[2])
    b = float(comment.split()[-2])
    lattice_constants = [a, b]

    # Replicar a célula unitária
    replicated_atoms = replicate_edge_crack(
        atoms, lattice_constants, n_replications_x, n_replications_y, crack_size)

    n_atoms_modified = replicated_atoms[0]
    atoms_modified = replicated_atoms[1]

    # Escrever o arquivo .xyz com a estrutura replicada
    write_xyz(OUTPUT_STRUCTURE_FILE, n_atoms_modified, comment, atoms_modified)

    print('Estrutura com rasgo em borda n1 replicada, arquivo salvo em {}'.format(
        OUTPUT_STRUCTURE_FILE))
