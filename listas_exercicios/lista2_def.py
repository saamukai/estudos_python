def hello_world():
    return 'Hello World!'

def master(function):
    return function()

executing = master(hello_world)
print(executing)

###########################
def master2(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def dizOi(nome):
    return f'Oi {nome}'

def saudar(saudacao, nome):
    return f'{saudacao} , {nome}!'

executing2 = master2(dizOi, "Nome")
print(executing2)
executing2 = master2(saudar, "Bom dia", "Nome")
print(executing2)
