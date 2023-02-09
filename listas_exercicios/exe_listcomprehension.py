'''Imagine uma string:
string = 0123456789012345678901234567890123456789
Obseerve que tem um padrão (1-9), separe esses grupos de 1-9
de forma que fique assim:
lista = [ '01234567891','0123456789','0123456789']
Usando list comprehension // retornando '0123456789.0123456789'''

string = '0123456789012345678901234567890123456789'

def separa_padrao(string):
    n = 10
    lista = [string[i:i+n] for i in range(0, len(string), n)]
    return ".".join(lista)

print(separa_padrao(string))
