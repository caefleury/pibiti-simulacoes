import math
# Ler o arquivo XYZ
def ler_xyz(arquivo):
    with open(arquivo, 'r') as f:
        n_atomos = int(f.readline())
        comentario = f.readline()
        atomos = []
        for linha in f:
            atomo, x, y, z = linha.split()
            atomos.append((atomo, [float(x), float(y), float(z)]))
    return n_atomos, comentario, atomos

# Replicar a célula unitária
def replicar_celula(atomos, vetores_rede, n_replicas_x, n_replicas_y):
    atomos_replicados = []
    for i in range(n_replicas_x):
        for j in range(n_replicas_y):
            for atomo, posicao in atomos:
                hipotenusa = 1.42
                cateto = math.sqrt(hipotenusa**2 / 2) 
                x_total = 2 * hipotenusa + 2 * cateto 
                y_total = hipotenusa + 2 * cateto
                nova_posicao = [posicao[0] + (x_total + vetores_rede[0]) * i , posicao[1] + (y_total + vetores_rede[1])*j , 0.0]
                atomos_replicados.append((atomo, nova_posicao))
    return atomos_replicados

# Escrever o arquivo XYZ
def escrever_xyz(arquivo, n_atomos, comentarios, atomos):
    with open(arquivo, 'w') as f:
        f.write(str(n_atomos) + '\n')
        f.write(comentarios + '\n')
        for atomo, posicao in atomos:
            x = format(posicao[0], '.16f')
            y = format(posicao[1], '.16f')
            z = format(posicao[2], '.16f')
            f.write('{} {} {} {}\n'.format(atomo, x, y, z))

# Parâmetros
arquivo_entrada = 'src/unit_cell.xyz'
n_replicas_x = 2
n_replicas_y = 1

# Ler a célula unitária
n_atomos, comentarios, atomos = ler_xyz(arquivo_entrada)

# Obter os vetores de rede
a = 6.3028
b = 4.9302

vetores_rede = [a,b]

# Replicar a célula unitária
atomos_replicados = replicar_celula(atomos, vetores_rede, n_replicas_x, n_replicas_y)

# Escrever o arquivo XYZ com a estrutura replicada
arquivo_saida = 'src/structure.xyz'
escrever_xyz(arquivo_saida, n_replicas_x * n_replicas_y * n_atomos, comentarios, atomos_replicados)

print('Estrutura replicada com sucesso! Arquivo salvo em {}'.format(arquivo_saida))
