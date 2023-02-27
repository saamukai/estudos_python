
with open('pessoas.csv') as arquivo: # é fechado automaticamente
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo fechado')
