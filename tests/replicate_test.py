

import pytest

from utils.my_utils import read_xyz

class TestReplicate():
    def test_read(self):
        test_file = 'tests/test_read.xyz'
        number_of_atoms, comment, atom_list = read_xyz(test_file)
        assert number_of_atoms == 10
        assert comment == 'a = 6.3028 Å and b = 4.9302 Å\n'
        assert atom_list == [
            ('C', [1.7314000000000003, 0.7510083707151027, 0.0]),
            ('C', [3.1514, 0.7510083707151027, 0.0]), 
            ('C', [4.571400000000001, 0.7510083707151027, 0.0]), 
            ('C', [5.5754916292848975, 1.7551, 0.0]), 
            ('C', [5.5754916292848975, 3.1751, 0.0]), 
            ('C', [4.571400000000001, 4.179191629284897, 0.0]), 
            ('C', [3.1514, 4.179191629284897, 0.0]), 
            ('C', [1.7314000000000003, 4.179191629284897, 0.0]), 
            ('C', [0.7273083707151029, 3.1751, 0.0]), 
            ('C', [0.7273083707151029, 1.7551, 0.0])]
        
