import csv
from time import sleep
from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
from options import initNav


# current_directory = path.dirname(path.abspath(__file__))
filename = '/home/saamukai/Desktop/repositorios/ssys/notifications/numeros.csv'
url_base = 'https://web.whatsapp.com/send?phone'
mensagem = '[VASCO INFORMA] enviada una mensaje a telefono del Grandioso'
navegador = initNav()
navegador.get("https://web.whatsapp.com/")

# while len(navegador.find_element("id", "side")) < 1:
#     sleep(1)

# with open(filename, 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     pular_head = next(csvreader)

#     for linha in csvreader:
#         nome = linha[0]
#         num = linha[1]
#         texto = quote(f'{nome}, {mensagem}')
#         link = f'{url_base}={num}&text={texto}'
#         navegador.get(link)
#         while len(navegador.find_element("id", "side")) < 1:
#             sleep(1)
#         navegador.find_element_by_xpath('''
#                     /html/body/div/div[1]/div[1]
#                     /div[4]/div[1]/footer/div[1]
#                     /div[2]/div/div[2]''').send_keys(Keys.ENTER)
#         sleep(10)
