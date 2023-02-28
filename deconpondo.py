num = int(input( ))

vetor = []

while num > 0:
    valor = num % 10
    #print(valor,end = ' ')
    vetor.insert(0, num % 10)
    num = num // 10
    
print(vetor)