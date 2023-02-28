n = int(input( ))

valores = [int(i) for i in input( ).split( )]

grupo1 = len(valores) // 2

soma1 = 0
for i in range (0, grupo1):
    soma1 = soma1 + valores[i]
    
soma2 = 0
for i in range(grupo1, len(valores) ):
    soma2 = soma2 + valores[i]
    
if soma1 > soma2:
    print('Jedi')
    
elif soma1 < soma2:
    print('Sith')

else:
    print('empate')