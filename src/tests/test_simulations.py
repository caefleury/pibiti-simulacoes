import pytest
import os.path
from utils.my_utils import return_file_data, write_strain_file, write_strain_x_folders, write_strain_y_folders


class TestStrain():
    def test_read(self):
        INPUT_TEST_FILE = 'src/utils/lammps_simulation_files/strain-x.in'
        file_data = return_file_data(INPUT_TEST_FILE)
        read_data = 'read_data       NOME.charge\n'
        pair_coeff = 'pair_coeff      * * CHO2008-kc2-enable.reaxff C\n'
        velocity = 'velocity    all create ${temperatura} 111111111 rot yes\n'
        assert file_data[7] == read_data
        assert file_data[13] == pair_coeff
        assert file_data[157] == velocity

    def test_write_file(self):
        INPUT_TEST_FILE = 'src/utils/lammps_simulation_files/strain-x.in'

        CHARGE_TEST_FILE_NAME = 'test.charge'
        REAXFF_TEST_FILE_NAME = 'test.reaxff'
        OUTPUT_STRAIN_TEST_FILE = 'src/tests/test_write.in'

        write_strain_file(OUTPUT_STRAIN_TEST_FILE,
                          INPUT_TEST_FILE,
                          CHARGE_TEST_FILE_NAME,
                          REAXFF_TEST_FILE_NAME,
                          pristine=True)

        read_data = 'read_data       test.charge\n'
        pair_coeff = 'pair_coeff      * * test.reaxff C\n'
        output_file_data = return_file_data(OUTPUT_STRAIN_TEST_FILE)

        assert output_file_data[7] == read_data
        assert output_file_data[13] == pair_coeff

    def test_write_x_folders(self):
        simulations_folders = ['center_crack',
                               'n1_x_axis_crack', 'n1_y_axis_crack']
        folder = 'src/tests/' + simulations_folders[0]
        strain_data = 'src/utils/lammps_simulation_files/strain-x.in'
        structure_charge_file = 'center_crack_structure.charge'
        reaxff_file = 'CHO2008-kc2-enable.reaxff'

        write_strain_x_folders(folder, strain_data,
                               structure_charge_file, reaxff_file, pristine=True)

        assert os.path.exists(folder + '/strain-x/1/CHO2008-kc2-enable.reaxff')
        assert os.path.exists(folder + '/strain-x/2/CHO2008-kc2-enable.reaxff')
        assert os.path.exists(folder + '/strain-x/3/CHO2008-kc2-enable.reaxff')
        assert os.path.exists(folder + '/strain-x/4/CHO2008-kc2-enable.reaxff')
        assert os.path.exists(folder + '/strain-x/5/CHO2008-kc2-enable.reaxff')

        assert os.path.exists(
            folder + '/strain-x/1/center_crack_structure.charge')
        assert os.path.exists(
            folder + '/strain-x/2/center_crack_structure.charge')
        assert os.path.exists(
            folder + '/strain-x/3/center_crack_structure.charge')
        assert os.path.exists(
            folder + '/strain-x/4/center_crack_structure.charge')
        assert os.path.exists(
            folder + '/strain-x/5/center_crack_structure.charge')

    def test_write_y_folders(self):
        simulations_folders = ['center_crack',
                               'n1_x_axis_crack', 'n1_y_axis_crack']
        folder = 'src/tests/' + simulations_folders[0]
        strain_data = 'src/utils/lammps_simulation_files/strain-y.in'
        structure_charge_file = 'center_crack_structure.charge'
        reaxff_file = 'CHO2008-kc2-enable.reaxff'

        write_strain_y_folders(folder, strain_data,
                               structure_charge_file, reaxff_file, pristine=True)

        assert os.path.exists(folder + '/strain-y/1/CHO2008-kc2-enable.reaxff')
        assert os.path.exists(folder + '/strain-y/2/CHO2008-kc2-enable.reaxff')
        assert os.path.exists(folder + '/strain-y/3/CHO2008-kc2-enable.reaxff')
        assert os.path.exists(folder + '/strain-y/4/CHO2008-kc2-enable.reaxff')
        assert os.path.exists(folder + '/strain-y/5/CHO2008-kc2-enable.reaxff')

        assert os.path.exists(
            folder + '/strain-y/1/center_crack_structure.charge')
        assert os.path.exists(
            folder + '/strain-y/2/center_crack_structure.charge')
        assert os.path.exists(
            folder + '/strain-y/3/center_crack_structure.charge')
        assert os.path.exists(
            folder + '/strain-y/4/center_crack_structure.charge')
        assert os.path.exists(
            folder + '/strain-y/5/center_crack_structure.charge')

    def test_update_strain_config_file(self):
        pass
