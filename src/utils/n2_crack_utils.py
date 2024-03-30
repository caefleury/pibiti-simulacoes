# Cracks in the y-axis
def y_left_crack(y_index, atom, n_replications_y,
                 crack_size, atom_index, new_position):
    floor = int(n_replications_y // 2 - ((crack_size - 1) / 2) + 1)
    ceiling = int(n_replications_y // 2 + ((crack_size - 1) / 2) - 1)
    if y_index in range(floor, ceiling + 1):
        atom = 'H'
        if (y_index == floor and atom_index in [0, 1, 2, 8, 9]) or (
                y_index == ceiling and atom_index in [5, 6, 7, 8, 9]):
            return [atom, new_position]
        else:
            if atom_index in [8, 9]:
                return [atom, new_position]
    else:
        return [atom, new_position]


def y_center_crack(y_index, atom, n_replications_y,
                   crack_size, atom_index, new_position):
    floor = int(n_replications_y // 2 - ((crack_size - 1) / 2))
    ceiling = int(n_replications_y // 2 + ((crack_size - 1) / 2))
    if y_index in range(floor, ceiling + 1):
        atom = 'H'
        if (y_index == floor and atom_index in [0, 1, 2, 3, 4, 8, 9]) or (
                y_index == ceiling and atom_index in [3, 4, 5, 6, 7, 8, 9]):
            return [atom, new_position]
    else:
        return [atom, new_position]


def y_right_crack(y_index, atom, n_replications_y,
                  crack_size, atom_index, new_position):
    floor = int(n_replications_y // 2 - ((crack_size - 1) / 2) + 1)
    ceiling = int(n_replications_y // 2 + ((crack_size - 1) / 2) - 1)
    if y_index in range(floor, ceiling + 1):
        atom = 'H'
        if (y_index == floor and atom_index in [0, 1, 2, 3, 4]) or (
                y_index == ceiling and atom_index in [3, 4, 5, 6, 7]):
            return [atom, new_position]
        else:
            if atom_index in [3, 4]:
                return [atom, new_position]
    else:
        return [atom, new_position]

# Cracks on the x-axis


def x_left_crack(x_index, atom, n_replications_x,
                 crack_size, atom_index, new_position):
    floor = int(n_replications_x // 2 - ((crack_size - 1) / 2) + 1)
    ceiling = int(n_replications_x // 2 + ((crack_size - 1) / 2) - 1)
    if x_index in range(floor, ceiling + 1):
        atom = 'H'
        if (x_index == floor and atom_index in [5, 6, 7, 8, 9]) or (
                x_index == ceiling and atom_index in [3, 4, 5, 6, 7]):
            return [atom, new_position]
        else:
            if atom_index in [0, 1, 2]:
                return [atom, new_position]
    else:
        return [atom, new_position]


def x_center_crack(x_index, atom, n_replications_x,
                   crack_size, atom_index, new_position):
    floor = int(n_replications_x // 2 - ((crack_size - 1) / 2))
    ceiling = int(n_replications_x // 2 + ((crack_size - 1) / 2))
    if x_index in range(floor, ceiling + 1):
        atom = 'H'
        if (x_index == floor and atom_index in [0, 1, 2, 5, 6, 7, 8, 9]) or (
                x_index == ceiling and atom_index in [0, 1, 2, 3, 4, 5, 6, 7]):
            return [atom, new_position]
    else:
        return [atom, new_position]


def x_right_crack(x_index, atom, n_replications_x,
                  crack_size, atom_index, new_position):
    floor = int(n_replications_x // 2 - ((crack_size - 1) / 2) + 1)
    ceiling = int(n_replications_x // 2 + ((crack_size - 1) / 2) - 1)
    if x_index in range(floor, ceiling + 1):
        atom = 'H'
        if (x_index == floor and atom_index in [8, 9, 0, 1, 2]) or (
                x_index == ceiling and atom_index in [0, 1, 2, 3, 4]):
            return [atom, new_position]
        else:
            if atom_index in [5, 6, 7]:
                return [atom, new_position]
    else:
        return [atom, new_position]
