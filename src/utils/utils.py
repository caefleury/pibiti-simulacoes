

def read_xyz(file):
    with open(file, 'r') as f:
        n_atoms = int(f.readline())
        comment = f.readline()
        atoms = []
        for line in f:
            atom, x, y, z = line.split()
            atoms.append((atom, [float(x), float(y), float(z)]))
    return n_atoms, comment, atoms


def write_xyz(file, n_atoms, comment, atoms):
    with open(file, 'w') as f:
        f.write(str(n_atoms) + '\n')
        f.write(comment)
        for atom, position in atoms:
            x = format(position[0], '.16f')
            y = format(position[1], '.16f')
            z = format(position[2], '.16f')
            f.write('{} {} {} {}\n'.format(atom, x, y, z))
