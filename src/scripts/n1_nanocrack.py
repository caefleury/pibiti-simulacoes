# Ler o arquivo XYZ
def read_xyz(file):
    with open(file, 'r') as f:
        n_atoms = int(f.readline())
        comment = f.readline()
        atoms = []
        for linha in f:
            atom, x, y, z = linha.split()
            atoms.append((atom, [float(x), float(y), float(z)]))
    return n_atoms, comment, atoms

# Replicar a célula unitária com os nanocracks lineares (n1)
def replicate_cell(atoms, lattice_constants, n_replications_x, n_replications_y):
    replicated_atoms = []
    for i in range(n_replications_x):
        for j in range(n_replications_y):
            for index,(atom, position) in enumerate(atoms):
                if i == 7:
                    atom = 'H'
                    if j < 7:
                        if j == 0:
                            new_position = [position[0] + (lattice_constants[0]) * i, position[1] + (lattice_constants[1])*j, 0.0]
                else:
                    new_position = [
                        position[0] + (lattice_constants[0]) * i, position[1] + (lattice_constants[1])*j, 0.0]
                replicated_atoms.append((atom, new_position))

            
    return replicated_atoms

# Escrever o arquivo .xyz
def write_xyz(file, n_atoms, comment, atoms):
    with open(file, 'w') as f:
        f.write(str(n_atoms) + '\n')
        f.write(comment + '\n')
        for atom, position in atoms:
            x = format(position[0], '.16f')
            y = format(position[1], '.16f')
            z = format(position[2], '.16f')
            f.write('{} {} {} {}\n'.format(atom, x, y, z))


# Vetores de rede (lattice constants)
a = 6.3028
b = 4.9302
lattice_constants = [a, b]

# Parâmetros
unit_cell_file = 'src/simulations/unit_cell.xyz'
n_replications_x = 15
n_replications_y = 15


# Ler a célula unitária
n_atoms, comment, atoms = read_xyz(unit_cell_file)

# Replicar a célula unitária
replicated_atoms = replicate_cell(
    atoms, lattice_constants, n_replications_x, n_replications_y)

# Escrever o arquivo .xyz com a estrutura replicada
OUTPUT_STRUCTURE_FILE = 'src/simulations/n1_nanocrack_structure.xyz'

write_xyz(OUTPUT_STRUCTURE_FILE, n_replications_x *
             n_replications_y * n_atoms, comment, replicated_atoms)

print('Estrutura replicada com sucesso! arquivo salvo em {}'.format(
    OUTPUT_STRUCTURE_FILE))
