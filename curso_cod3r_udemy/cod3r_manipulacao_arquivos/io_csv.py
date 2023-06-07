import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada): # ja trata a 'formatacao' do arquivo csv
        print('Nome: {}, Idade {}'.format(*pessoa))

