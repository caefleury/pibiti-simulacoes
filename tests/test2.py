import math

hip = 1.42


def calculaCatetos(hipotenusa):
    cateto = math.sqrt(hipotenusa**2 / 2)
    return cateto


cateto = calculaCatetos(hip)
print(cateto)

x1 = [cateto, 0, 0]
x2 = [cateto+hip, 0, 0]
x3 = [cateto+hip*2, 0, 0]
x4 = [cateto+hip*2+cateto, cateto, 0]
x5 = [cateto+hip*2+cateto, cateto+hip, 0]
x6 = [cateto+hip*2, cateto*2+hip, 0]
x7 = [cateto+hip, cateto*2+hip, 0]
x8 = [cateto, cateto*2+hip, 0]
x9 = [0, cateto+hip, 0]
x10 = [0, cateto, 0]


def padraoAtomo(atomo):
    x, y, z = atomo
    x = format(x, '.16f')
    y = format(y, '.16f')
    z = format(z, '.16f')
    return f"C       {x}       {y}       {z}"


lista = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
listaPadrao = [padraoAtomo(atomo) for atomo in lista]

with open('test2.xyz', 'a') as file:
    for atomo in listaPadrao:
        file.write(atomo + '\n')
