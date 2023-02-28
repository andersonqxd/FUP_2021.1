from math import * 


def potencia(base, expoente):
    pot = 1
    for o in range (1, expoente + 1):
        pot = base * pot
        
    return pot

def distancia (ax, ay,  bx, by):
    d = sqrt( potencia( (ax - bx), 2 ) + potencia( (ay - by), 2 ) )
    
    return d 
    
ax = float(input( ))
ay = float(input( ))
bx = float(input( ))
by = float(input( ))

dist  = distancia(ax, ay,  bx, by)
print('%.2f' % dist)


