

from my_utils import read_xyz, write_xyz
from n2_crack_utils import y_left_crack, y_center_crack, y_right_crack, x_left_crack, x_center_crack, x_right_crack

# Replicar a célula unitária com os nanocracks lineares (n2)


def replicate_n2_crack(atoms, lattice_constants, n_replications_x,
                       n_replications_y, crack_size, crack_direction):
    replicated_atoms = []
    for x in range(n_replications_x):
        for y in range(n_replications_y):
            for index, (atom, position) in enumerate(atoms):
                # POSICOES PERMANECEM CONSTANTES
                new_position = [
                    position[0] + (lattice_constants[0]) * x, position[1] + (lattice_constants[1]) * y, 0.0]
                if crack_direction == 'y':
                    if x == (n_replications_x // 2 - 1):
                        if y_left_crack(y, atom, n_replications_y,
                                        crack_size, index, new_position):
                            atom, new_position = y_left_crack(
                                y, atom, n_replications_y, crack_size, index, new_position)
                            replicated_atoms.append((atom, new_position))

                    elif x == (n_replications_x // 2):
                        if y_center_crack(
                                y, atom, n_replications_y, crack_size, index, new_position):
                            atom, new_position = y_center_crack(
                                y, atom, n_replications_y, crack_size, index, new_position)
                            replicated_atoms.append((atom, new_position))

                    elif x == (n_replications_x // 2 + 1):
                        if y_right_crack(
                                y, atom, n_replications_y, crack_size, index, new_position):
                            atom, new_position = y_right_crack(
                                y, atom, n_replications_y, crack_size, index, new_position)
                            replicated_atoms.append((atom, new_position))
                    else:
                        replicated_atoms.append((atom, new_position))
                else:
                    if y == (n_replications_y // 2 - 1):
                        if x_left_crack(x, atom, n_replications_x,
                                        crack_size, index, new_position):
                            atom, new_position = x_left_crack(
                                x, atom, n_replications_x, crack_size, index, new_position)
                            replicated_atoms.append((atom, new_position))

                    elif y == (n_replications_y // 2):
                        if x_center_crack(
                                x, atom, n_replications_x, crack_size, index, new_position):
                            atom, new_position = x_center_crack(
                                x, atom, n_replications_x, crack_size, index, new_position)
                            replicated_atoms.append((atom, new_position))

                    elif y == (n_replications_y // 2 + 1):
                        if x_right_crack(
                                x, atom, n_replications_x, crack_size, index, new_position):
                            atom, new_position = x_right_crack(
                                x, atom, n_replications_x, crack_size, index, new_position)
                            replicated_atoms.append((atom, new_position))
                    else:
                        replicated_atoms.append((atom, new_position))

    return [len(replicated_atoms), replicated_atoms]


def run(replications_x, replications_y, crack_direction):
    # Parâmetros
    INPUT_UNIT_CELL_FILE = 'src/xyz_structures/unit_cell.xyz'
    OUTPUT_STRUCTURE_FILE = 'src/xyz_structures/n2_crack_structure.xyz'
    crack_size = 9

    # Ler a célula unitária
    n_atoms, comment, atoms = read_xyz(INPUT_UNIT_CELL_FILE)

    # Vetores de rede (lattice constants)
    a = float(comment.split()[2])
    b = float(comment.split()[-2])
    lattice_constants = [a, b]

    # Replicar a célula unitária
    replicated_atoms = replicate_n2_crack(
        atoms, lattice_constants, replications_x, replications_y, crack_size, crack_direction)

    n_atoms_modified = replicated_atoms[0]
    atoms_modified = replicated_atoms[1]

    # Escrever o arquivo .xyz com a estrutura replicada
    write_xyz(OUTPUT_STRUCTURE_FILE, n_atoms_modified, comment, atoms_modified)

    print('Estrutura com rasgo n2 replicada, arquivo salvo em {}'.format(
        OUTPUT_STRUCTURE_FILE))
