variavel = 'valor' ## variavel global
variavel2 = 'valor global'
variavel3 = 'valor global 3'

def func():
    print(variavel)


def func2():
    variavel = 'Outro valor' ## variável local, portanto não a global não é alterada
    print(variavel)

func()
func2()

print(variavel)

def alteraGlobalErrado():
    global variavel2
    variavel2 = 'Outro valor var2'
    print (variavel2)

alteraGlobalErrado()

def alteraGlobalCerto(arg=None):
    arg = arg.replace('v', 'c')
    return arg

outra_var = alteraGlobalCerto(arg=variavel3)
print(outra_var)


### var local:

def funcVarLoc():
    outra_var2 = 'Nome'
    return outra_var2

def func2VarLoc(arg):
    print(arg)

var = funcVarLoc()
func2VarLoc(var)
