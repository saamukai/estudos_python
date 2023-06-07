import csv

with open('desafio-ibge.csv', encoding='ISO-8859-1') as dados:
    with open('saida.txt', 'w') as saida:
        for cidade in csv.reader(dados):
            print(f'{cidade[8]}: {cidade[3]}', file=saida)
