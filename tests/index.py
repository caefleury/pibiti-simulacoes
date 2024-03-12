


n_replications_y = 15
crack_size = 7

floor = int(n_replications_y//2 - ((crack_size - 1)/2)) # 4
ceiling = int(n_replications_y//2 + ((crack_size - 1)/2))  # 10

print(floor)
print(ceiling)
print('-----------------------')

crack_size = 5

floor = int(n_replications_y//2 - ((crack_size - 1)/2)) # 5
ceiling = int(n_replications_y//2 + ((crack_size - 1)/2))  # 9

print(floor)
print(ceiling)
print('-----------------------')

print("laterals")

crack_size = 7

floor = int(n_replications_y//2 - ((crack_size - 1)/2) + 1) # 5
ceiling = int(n_replications_y//2 + ((crack_size - 1)/2) - 1)  # 9





"""
elif i == n_replications_x // 2:  # CENTRO DA FOLHA - (7 para 15x15)
                    # INICIO DO CRACK 3X1
                    if j in [6, 7, 8]:  # TERMINAR NA MOLECULA 7X8 (j < 8)
                        # MOLECULA INICIAL DO CRACK EM UMA LINHA (começando na molecula 7x6)
                        if j == 6:  # j == 6
                            if index in [0, 1, 2, 3, 4, 8, 9]:
                                atom = 'H'
                                replicated_atoms.append((atom, new_position))
                        elif j == 7:  # MOLECULA DO CENTRO (j ==7)
                            if index in [3, 4, 8, 9]:
                                atom = 'H'
                                replicated_atoms.append((atom, new_position))
                        elif j == 8:  # (j==8)
                            if index in [3, 4, 5, 6, 7, 8, 9]:
                                atom = 'H'
                                replicated_atoms.append((atom, new_position))

def central_crack(cell_type,index): # type = top,bottom
    if cell_type == 'top':
        if index in [3, 4, 8, 9]: 
            atom = 'H'
            replicated_atoms.append((atom, new_position))
        return []
    elif cell_type == 'mid':
        pass

def lateral_crack(crack_side,cell_type,index):
    pass
"""