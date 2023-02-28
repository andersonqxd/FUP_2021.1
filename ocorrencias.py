frase = input()
procurado = input()

cont = 0
for char in frase:
    if char == procurado:
        cont += 1
        
print(cont)