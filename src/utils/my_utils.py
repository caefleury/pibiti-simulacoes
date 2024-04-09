import random

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

def read_strain_file(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data


def write_strain_file(file,strain_data,structure_file,reaxff_file):
    random_int = random.randint(100000000, 999999999)
    read_data = f'read_data       {structure_file}\n'
    velocity = 'velocity    all create ${temperatura} % rot yes\n' % (str(random_int))
    pair_coeff = f'pair_coeff      * * {reaxff_file} C\n'
    with open(file, 'w') as f:
        for i,line in enumerate(strain_data):
            if i == 7:
                f.write(read_data)
            elif i == 13:
                f.write(pair_coeff)
            elif i == 157:
                f.write(velocity)
            else:
                f.write(str(line)+'\n')

# "Hello, %s. You are %d years old." % (name, age)