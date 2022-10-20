nome = input("Digite o seu primeiro nome: ")

if nome.isalpha:
    contaNome = len(nome)
    if contaNome <= 4:
        print("Seu nome é curto")
    if contaNome >=5 and contaNome <= 6:
        print("Seu nome é normal")
    if contaNome > 6:
        print("Seu nome é muito grande")
else:
    print("Digite somente um nome/um nome válido")