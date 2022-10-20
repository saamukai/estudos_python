hora = input("Digite que horas são: ")

if hora.isnumeric and int(hora)>=0:
    hora = int(hora)
    if hora >= 0 and hora<=11:
        print("Bom dia")
    elif hora >= 12 and hora <=17:
        print("Boa tarde")
    elif hora >= 18 and hora <= 23:
        print("Boa tarde")
else:
    print("Digite um numero válido")
