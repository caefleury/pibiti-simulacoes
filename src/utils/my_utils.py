import random
import os
import shutil


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


def return_file_data(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data


def write_strain_file(file, strain_data_file, structure_charge_file, reaxff_file, pristine):
    strain_data = return_file_data(strain_data_file)
    random_int = random.randint(100000000, 999999999)
    read_data = f'read_data       {structure_charge_file}\n'
    velocity = "velocity    all create ${temperatura} %d rot yes\n" % (
        random_int)
    if pristine:
        pair_coeff = f'pair_coeff      * * {reaxff_file} C\n'
    else:
        pair_coeff = f'pair_coeff      * * {reaxff_file} C H\n'
    with open(file, 'w') as f:
        for i, line in enumerate(strain_data):
            if i == 7:
                f.write(read_data)
            elif i == 13:
                f.write(pair_coeff)
            elif i == 157:
                f.write(velocity)
            else:
                f.write(str(line))


def write_strain_x_folders(folder, x_strain_data, structure_charge_file, reaxff_file, pristine):
    reaxff_kc2_file = 'src/utils/lammps_simulation_files/CHO2008-kc2-enable.reaxff'
    for i in range(1, 6):
        current_folder = f'{folder}/strain-x/{i}'
        os.makedirs(current_folder, exist_ok=True)
        shutil.copy(reaxff_kc2_file, current_folder)
        shutil.copy('src/charge_structures/' +
                    structure_charge_file, current_folder)
        write_strain_file(current_folder + '/strain-x.in',
                          x_strain_data, structure_charge_file, reaxff_file, pristine)


def write_strain_y_folders(folder, y_strain_data, structure_charge_file, reaxff_file, pristine):
    reaxff_kc2_file = 'src/utils/lammps_simulation_files/CHO2008-kc2-enable.reaxff'
    for i in range(1, 6):
        current_folder = f'{folder}/strain-y/{i}'
        os.makedirs(current_folder, exist_ok=True)
        shutil.copy(reaxff_kc2_file, current_folder)
        shutil.copy('src/charge_structures/' +
                    structure_charge_file, current_folder)
        write_strain_file(current_folder + '/strain-y.in',
                          y_strain_data, structure_charge_file, reaxff_file, pristine)


def write_melting_file(file, melting_data_file):
    melting_data = return_file_data(melting_data_file)
    random_int = random.randint(100000000, 999999999)
    velocity = "velocity    all create ${temperatura_inicial} %d rot yes\n" % (
        random_int)
    with open(file, 'w') as f:
        for i, line in enumerate(melting_data):
            if i == 144:
                f.write(velocity)
            else:
                f.write(str(line))


def write_melting_seeds(folder, melting_data_file, structure_charge_file, reaxff_file):
    reaxff_kc2_file = 'src/utils/lammps_simulation_files/CHO2008-kc2-enable.reaxff'
    for i in range(1, 6):
        current_folder = f'{folder}/melting/{i}'
        os.makedirs(current_folder, exist_ok=True)
        shutil.copy(reaxff_kc2_file, current_folder)
        shutil.copy('src/charge_structures/' +
                    structure_charge_file, current_folder)
        write_melting_file(current_folder + '/melting.in',
                           melting_data_file)


def update_strain_config_file():
    pass
