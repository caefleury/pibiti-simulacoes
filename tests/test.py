import math



def calculaCatetos(hipotenusa):
    cateto = math.sqrt(hipotenusa**2 / 2) 
    return cateto

hip = 1.42
half = hip / 2
cateto = calculaCatetos(hip)

altura_total = 1.42 * 2 + cateto * 2

print(altura_total)

x1 = [cateto+hip+half,half,0]
x2 = [cateto+2*hip+half,half,0]
x3 = [cateto+3*hip+half,half,0]

x4 = [cateto+hip+half,half+altura_total,0]
x5 = [cateto+2*hip+half,half+altura_total,0]
x6 = [cateto+3*hip+half,half+altura_total,0]

x7 = [half,half+cateto,0]
x8 = [half,half+cateto+hip,0]

x9 = [half+cateto*2+3*hip,half,0] #x7
x10 = [half+cateto*2+3*hip,half+cateto+hip,0] #x8

def padraoAtomo(atomo):
    x,y,z = atomo
    x = format(x, '.16f')
    y = format(y, '.16f')
    z = format(z, '.16f')
    return f"C       {x}       {y}       {z}"

lista = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
listaPadrao = [padraoAtomo(atomo) for atomo in lista]

for atomo in listaPadrao:
    print(atomo)


print(f"x1: {x1}")
print(f"x2: {x2}")
print(f"x3: {x3}")
print(f"x4: {x4}")
print(f"x5: {x5}")
print(f"x6: {x6}")
print(f"x7: {x7}")
print(f"x8: {x8}")
print(f"x9: {x9}")
print(f"x10: {x10}")

print(hip*2+cateto*2+1.42+6.3028)
print(f"x_total = {hip*2+cateto*2}")
