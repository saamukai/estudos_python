def func (*args):
    print(args)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
n2 = 100
func(*lista, *lista2, n2, lista)
