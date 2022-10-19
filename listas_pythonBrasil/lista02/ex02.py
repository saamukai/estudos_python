num = input("Digite um numero inteiro: ")

if num.isnumeric() == True:
    num =int(num)
    if num % 2 == 0:
        print("O numero é par")
    else:
        print("O numero não é par")
else:
    print("O número não inteiro")
