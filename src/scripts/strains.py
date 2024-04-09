from my_utils import read_strain_file,write_strain_file

STRAIN_FILE_INPUT = 'src/utils/strain-x.in'

strain_data = read_strain_file(STRAIN_FILE_INPUT)

simulations = ['unit_crack','x_axis_crack','y_axis_crack']

def run():
    pass
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