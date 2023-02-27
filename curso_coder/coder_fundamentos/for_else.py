from random import randint

def sortearDado():
    return randint(1,6)

if __name__=='__main__':
    for i in range(1,7):
        if i%2 != 0:
            continue

        if i==sortearDado():
            print('Acertou', i)
            break

    else:
        print('Não acertou', i)
