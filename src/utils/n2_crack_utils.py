
def left_crack(y_index, atom, n_replications_y, crack_size, atom_index, new_position):
    floor = int(n_replications_y//2 - ((crack_size - 1)/2) + 1)
    ceiling = int(n_replications_y//2 + ((crack_size - 1)/2) - 1)
    if y_index in range(floor, ceiling+1):
        atom = 'H'
        if (y_index == floor and atom_index in [0, 1, 2, 8, 9]) or (y_index == ceiling and atom_index in [5, 6, 7, 8, 9]):
            return [atom, new_position]
        else:
            if atom_index in [8, 9]:
                return [atom, new_position]
    else:
        return [atom, new_position]


def center_crack(y_index, atom, n_replications_y, crack_size, atom_index, new_position):
    floor = int(n_replications_y//2 - ((crack_size - 1)/2))
    ceiling = int(n_replications_y//2 + ((crack_size - 1)/2))
    if y_index in range(floor, ceiling+1):
        atom = 'H'
        if (y_index == floor and atom_index in [0, 1, 2, 3, 4, 8, 9]) or (y_index == ceiling and atom_index in [3, 4, 5, 6, 7, 8, 9]):
            return [atom, new_position]
    else:
        return [atom, new_position]


def right_crack(y_index, atom, n_replications_y, crack_size, atom_index, new_position):
    floor = int(n_replications_y//2 - ((crack_size - 1)/2) + 1)
    ceiling = int(n_replications_y//2 + ((crack_size - 1)/2) - 1)
    if y_index in range(floor, ceiling+1):
        atom = 'H'
        if (y_index == floor and atom_index in [0, 1, 2, 3, 4]) or (y_index == ceiling and atom_index in [3, 4, 5, 6, 7]):
            return [atom, new_position]
        else:
            if atom_index in [3, 4]:
                return [atom, new_position]
    else:
        return [atom, new_position]
