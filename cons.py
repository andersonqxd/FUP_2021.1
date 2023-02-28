def  letra (c):
    if c >= 'a' and c <='z':
        return True
    elif c >= 'A' and c <= 'Z':
        return True
        
    else:
        return False

def vogal (c):
    vogais = 'aeiouAEIOU'
    for v in vogais:
        if c == v:
            return True
    return False
            
def cons (c):
    if not vogal(c) and letra(c):
        return True
    else:
        return False
        
frase = input()

for c in range(len(frase)):
    if cons(frase[c]) == True:
        print(c, end=' ')
    
        

