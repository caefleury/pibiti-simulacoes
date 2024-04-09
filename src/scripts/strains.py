import os
from my_utils import read_strain_file, write_strain_x_folders, write_strain_y_folders


def run():
    simulations_folders = ['pristine', 'center_crack',
                           'x_axis_crack']
    path = 'src/simulations/'
    for folder in simulations_folders:
        os.makedirs(f'src/simulations/{folder}', exist_ok=True)
        os.makedirs(f'src/simulations/{folder}/strain-x', exist_ok=True)
        os.makedirs(f'src/simulations/{folder}/strain-y', exist_ok=True)

        strain_x_data = 'src/utils/lammps_simulation_files/strain-x.in'
        strain_y_data = 'src/utils/lammps_simulation_files/strain-y.in'
        reaxff_file = 'CHO2008-kc2-enable.reaxff'

        if folder == 'pristine':
            structure_charge_file = 'pristine_structure.charge'
        elif folder == 'center_crack':
            structure_charge_file = 'center_crack_structure.charge'
        elif folder == 'x_axis_crack':
            structure_charge_file = 'n1_x_axis_crack_structure.charge'

        folder = f'src/simulations/{folder}'
        write_strain_x_folders(folder, strain_x_data,
                               structure_charge_file, reaxff_file)

        write_strain_y_folders(folder, strain_y_data,
                               structure_charge_file, reaxff_file)
        
        print(f"Criando Simulação: {folder}")

# CRIAR LISTA COM O NOME DE TODAS AS ESTRUTURAS
# FOR LOOP DA ESTRUTURA
    # CRIAR FOLDER PARA A ESTRUTURA = STRUCTURE_FILE
    # CRIAR FOLDER DO STRAIN X DENTRO DO STRUCTURE_FILE
    # CRIA FOLDER DO STRAIN Y DENTRO DO STRUCTURE_FILE
    # FOR LOOP DO STRAIN X
        # CRIA PASTA
        # CRIA STRAIN X CORRESPONDENTE
        # POPULA PASTA COM OS OUTROS 3 ARQUIVOS
    # FOR LOOP DO STRAIN Y
        # CRIA PASTA
        # CRIA STRAIN X CORRESPONDENTE
        # POPULA PASTA COM OS OUTROS 3 ARQUIVOS

        