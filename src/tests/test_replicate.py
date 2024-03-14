

import pytest

from utils.my_utils import read_xyz,write_xyz

class TestReplicate():
    
    def test_write(self):
        test_file = 'src/tests/test_write.xyz'
        number_of_atoms = 3
        comment = 'a = 6.3028 Å and b = 4.9302 Å\n'
        atom_list = [
            ('C', [1.7314000000000003, 0.7510083707151027, 0.0]),
            ('C', [3.1514, 0.7510083707151027, 0.0]), 
            ('C', [4.571400000000001, 0.7510083707151027, 0.0])
        ]
        write_xyz(test_file,number_of_atoms,comment,atom_list)

        number_of_atoms, comment, atom_list = read_xyz(test_file)
        assert number_of_atoms == 3
        assert comment == 'a = 6.3028 Å and b = 4.9302 Å\n'
        assert atom_list == [
            ('C', [1.7314000000000003, 0.7510083707151027, 0.0]),
            ('C', [3.1514, 0.7510083707151027, 0.0]), 
            ('C', [4.571400000000001, 0.7510083707151027, 0.0])
        ]
    