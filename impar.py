matriz = []
for m in range(5):
    matriz.append([int(i) for i in input().split()])
    
cont = 0
for l in range(0, len(matriz)):
    for c in range(l + 1, len(matriz)):
        if (matriz[l][c]) % 2 != 0:
            cont += 1
            
            
for l in range(len(matriz)):
    for c in range(len(matriz)):
        if l == c:
            matriz[l][c] = cont
            
print(matriz)