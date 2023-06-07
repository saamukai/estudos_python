t1 = (1,2,3,'a','Samuel')
print(type(t1))
print(t1)

print(t1[1:])

for indice in t1:
    print(indice)

t2 = 1,2,'a' # tambem pode ser declarada dessa forma
print(t2[0:])

#atencao
# t3 = 1 # isso vai criar uma variavel e n uma tupla (tem q ter virgula)

t3 = t1 + t2

print(t3)

# TUPLAS NAO SÃO EDITÁVEIS
# CONVERTA EM LISTA

t3 = list(t3)
t3[1] = 'novo valor'
print(t3)
