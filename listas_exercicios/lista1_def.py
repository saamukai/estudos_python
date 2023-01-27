
####################
def saudacao (saudacao, nome):
    print(f"{saudacao}, {nome}")


saudacao("Olá, bom dia", "Samuel")

######################
def soma (n1, n2, n3):
    return float(n1 + n2 + n3)

print(soma(2,1,3))

######################
def percent(n1,n2):
    return (n1+((n2/100)*n1))

print(percent(85.20, 2.7))

######################
def fizzBuzz(num):
    if num%5 == 0 and num%3 == 0:
        return "FizzzBuzz"
    if num%3 == 0:
        return "fizz"
    if num%5 == 0:
        return "buzz"

    return num

print(fizzBuzz(20))
