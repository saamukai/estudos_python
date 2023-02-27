PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida',
    'bagulho é a copa e religiao'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto possui palavras probidas: ', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado: ', texto)
