import math

hip = 1.42
cateto = math.sqrt((hip**2) / 2) # 1.0023

a = 6.3028
b = 4.9302
x = (a - ((2*cateto) + (2*hip))) / 2 # 0.7238
y = (b - (hip + (2*cateto))) / 2 # 0.75

x1 = [x+cateto,                  y,                 0.0]
x2 = [x+cateto+hip,              y,                 0.0]
x3 = [x+cateto+(2*hip),          y,                 0.0]       

x4 = [x+(2*cateto)+(2*hip),      y+cateto,          0.0]
x5 = [x+(2*cateto)+(2*hip),      y+cateto+hip,      0.0]

x6 = [x+cateto+(2*hip),      y+(2*cateto)+hip,      0.0]
x7 = [x+cateto+hip,          y+(2*cateto)+hip,      0.0]
x8 = [x+cateto,              y+(2*cateto)+hip,      0.0]

x9 = [x,                     y+cateto+hip,          0.0] 
x10= [x,                     y+cateto,              0.0] 

def padraoAtomo(atomo):
    x,y,z = atomo
    x = format(x, '.16f')
    y = format(y, '.16f')
    z = format(z, '.16f')
    return f"C       {x}       {y}       {z}"

lista = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
listaPadrao = [padraoAtomo(atomo) for atomo in lista]

with open('tests/test.xyz', 'w') as file:
    file.write(str(len(listaPadrao)) + '\n')
    for atomo in listaPadrao:
        file.write(atomo + '\n')
