
# Ler o arquivo XYZ
def read_xyz(file):
    with open(file, 'r') as f:
        n_atoms = int(f.readline())
        comment = f.readline()
        atoms = []
        for line in f:
            atom, x, y, z = line.split()
            atoms.append((atom, [float(x), float(y), float(z)]))
    return n_atoms, comment, atoms

# Replicar a célula unitária com os nanocracks lineares (n1)
def replicate_cell(atoms, lattice_constants, n_replications_x, n_replications_y):
    replicated_atoms = []
    for i in range(n_replications_x):
        for j in range(n_replications_y):
            for index,(atom, position) in enumerate(atoms):
                # POSICOES PERMANECEM CONSTANTES
                new_position = [position[0] + (lattice_constants[0]) * i, position[1] + (lattice_constants[1])*j, 0.0]
                if i == 2: # CENTRO DA FOLHA - (7 para 15x15)
                    # INICIO DO CRACK 3X1
                    if j in [1,2,3]: # TERMINAR NA MOLECULA 7X8 (j < 8)
                        # MOLECULA INICIAL DO CRACK EM UMA LINHA (começando na molecula 7x6)
                        if j == 1: # j == 6
                            if index in [0,1,2,3,4,8,9]:
                                atom = 'H'
                                replicated_atoms.append((atom, new_position))
                        elif j == 2: # MOLECULA DO CENTRO (j ==7)
                            if index in [3,4,8,9]:
                                atom = 'H'
                                replicated_atoms.append((atom, new_position))
                        elif j == 3: #(j==8)
                            if index in [3,4,5,6,7,8,9]:
                                atom = 'H'
                                replicated_atoms.append((atom, new_position))
                    else:  
                        replicated_atoms.append((atom, new_position))
                else:
                    replicated_atoms.append((atom, new_position))
    return [len(replicated_atoms),replicated_atoms]

# Escrever o arquivo .xyz
def write_xyz(file, n_atoms, comment, atoms):
    with open(file, 'w') as f:
        f.write(str(n_atoms) + '\n')
        f.write(comment)
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
n_replications_x = 5
n_replications_y = 5

OUTPUT_STRUCTURE_FILE = 'src/simulations/n1_nanocrack_structure.xyz'

# Ler a célula unitária
n_atoms, comment, atoms = read_xyz(unit_cell_file)

# Replicar a célula unitária
replicated_atoms = replicate_cell(atoms, lattice_constants, n_replications_x, n_replications_y)

n_atoms_modified = replicated_atoms[0]
atoms_modified = replicated_atoms[1]

# Escrever o arquivo .xyz com a estrutura replicada
write_xyz(OUTPUT_STRUCTURE_FILE, n_atoms_modified, comment, atoms_modified)

print('Estrutura replicada, arquivo salvo em {}'.format(OUTPUT_STRUCTURE_FILE))
