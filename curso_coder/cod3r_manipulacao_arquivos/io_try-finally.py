
try: #codigo 'arriscado'
    arquivo = open('./pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally: #garate que o arquivo vai ser fechado
    # vai ser executado de toda forma, mas talvez o restante nao
    print('finally')
    arquivo.close()


if arquivo.closed:
    print('Arquvo já foi fechado!')
