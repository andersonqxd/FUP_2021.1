def vogal( c ):
    vogais = "aeiouAEIOU"
    for v in vogais:
        if c == v:
            return True
    return False

def letra( c ):
    if c >= 'a' and c <= 'z':
        return True
    elif c >= 'A' and c <= 'Z':
        return True
    else:
        return False

def cons( c ):
    if not vogal(c) and letra(c):
        return True
    else:
        return False



frase = input()

vogais = ""
consoantes = ""
for c in frase:
    if vogal(c):
        vogais += c
    elif cons(c):
        consoantes += c

print(vogais)
print(consoantes)






# frase = input()
# print( frase.upper() )
# print( "".join( [ c.upper() for c in frase ] ) )


