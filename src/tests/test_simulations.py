import pytest

from utils.my_utils import read_strain_file,write_strain_file


class TestStrain():
    def test_read(self):
        INPUT_TEST_FILE = 'src/utils/strain-x.in'
        file_data = read_strain_file(INPUT_TEST_FILE)
        read_data = 'read_data       pristine_structure.charge\n'
        pair_coeff = 'pair_coeff      * * CHO2008-kc2-enable.reaxff C\n'
        velocity = 'velocity    all create ${temperatura} 111111111 rot yes\n'
        assert file_data[7] == read_data
        assert file_data[13] == pair_coeff
        assert file_data[157] == velocity

    def test_write(self):
        INPUT_TEST_FILE = 'src/utils/strain-x.in'
        
        CHARGE_TEST_FILE_NAME = 'test.charge'
        REAXFF_TEST_FILE_NAME = 'test.reaxff'
        OUTPUT_STRAIN_TEST_FILE = 'src/tests/test_write.in'
        input_file_data = read_strain_file(INPUT_TEST_FILE)

        write_strain_file(OUTPUT_STRAIN_TEST_FILE,
                          input_file_data,
                          REAXFF_TEST_FILE_NAME,
                          CHARGE_TEST_FILE_NAME)
        
        read_data = 'read_data       test.charge\n'
        pair_coeff = 'pair_coeff      * * CHO2008-kc2-enable.reaxff C\n'
        velocity = 'velocity    all create ${temperatura} 111111111 rot yes\n'
        output_file_data = read_strain_file(OUTPUT_STRAIN_TEST_FILE)

        assert output_file_data[7] == read_data
        assert output_file_data[13] == pair_coeff
        assert output_file_data[157] == velocity



