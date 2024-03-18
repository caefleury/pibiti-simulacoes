

def center_crack(y_index, atom, n_replications_y, crack_size, atom_index, new_position):
    floor = int(n_replications_y//2 - ((crack_size - 1)/2))
    ceiling = int(n_replications_y//2 + ((crack_size - 1)/2))
    if y_index in range(floor, ceiling+1):
        atom = 'H'
        if (y_index == floor and atom_index in [0, 1, 2, 3, 4, 8, 9]) or (y_index == ceiling and atom_index in [3, 4, 5, 6, 7, 8, 9]):
            return [atom, new_position]
        elif atom_index in [2, 3, 8, 9]:
            return [atom, new_position]
    else:
        return [atom, new_position]
