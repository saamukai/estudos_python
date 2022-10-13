import time
import os
import random
import RLB_teste_DB
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def atualizaDB():
    pesquisa = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
    pesquisa.click()
    pesquisa.send_keys(Keys.ARROW_DOWN)
    nome = "Temp"
    celular = "Temp"
    while True:
        try:
            time.sleep(0.3)
            nome = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span').get_attribute('innerHTML').strip().replace('&nbsp;', ' ')
            if '+' in nome:
                celular, nome = nome, ''
            if celular == "Temp":
                driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/header').click()
                time.sleep(0.3)
                try:
                    celular = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[4]/div[3]/div/div/span/span').get_attribute('innerHTML').strip()
                except NoSuchElementException:
                    try:
                        celular = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[3]/div/div/span/span').get_attribute('innerHTML').strip()
                    except NoSuchElementException:
                        celular = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[7]/div[3]/div/div/span/span').get_attribute('innerHTML')
            RLB_teste_DB.addcontato(RLB_teste_DB.conecta(), nome, celular)
            nome, celular= 'Temp', 'Temp'
            selecionado = driver.find_element_by_xpath('//div[@aria-selected="true" and @role="row"]').send_keys(Keys.ARROW_DOWN)
        except Exception as e:
            print(e)
            continue


def contatafreelas(wpp, nome):
    if nome == "teste":
        contatos = (("Kato", "+5516991370464"), ("eh", "+5521993944353"), ("joao", "+5521972140343"))
    else:
        contatos = RLB_teste_DB.buscacontatoativo(RLB_teste_DB.conecta(), nome)
    jaForam = []
    for escolhido in contatos:
       # escolhido = random.choice(contatos)
       # if escolhido not in jaForam: jaForam.append(escolhido)
       # print(jaForam)
        print(f"Enviando mensagem para {escolhido[0].title()}({escolhido[1]})")
        wpp.get(f"https://web.whatsapp.com/send?phone={escolhido[1].replace('-', '').replace(' ', '')}&source=&data=#")
        pulaContato = ["+55 31 9216-3979",# Mariane Teotônio Eng Mecânica/ Química
                       "+55 19 98893-8083",
                       "+55 21 99669-6579",
                       "+55 31 8417-9037",
                       "+55 11 98197-9767",
                       "+55 19 98306-4193",
                       "+55 61 9959-1216",
                       "+55 12 99648-8800",
                       "+55 11 97243-8664",
                       "+55 62 9436-8212",
                       "+55 34 9201-4507",
                       "+55 79 9910-6931",
                       "+55 13 99775-0888",
                       "+55 11 94272-5373",
                       "+55 19 97122-1617",
                       "+55 86 8852-8716",
                       ]
        if escolhido[1] in pulaContato:
                pass
        else:
            time.sleep(3)
            txt = wpp.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[1]/div/div[2]")
            time.sleep(1.5)
            txt.send_keys(f"Olá {escolhido[0].title()}, você teria interesse de fazer um trabalho de freelancer?")
            txt.send_keys(Keys.ENTER)
            filepath = ('D:\DONWLOAD\\Prova_Arquitetura.rar')
            with open("mensagem2.txt", "r", encoding="utf-8") as msg:
                for line in msg:
                    txt.send_keys(str(line).strip())
                    txt.send_keys(Keys.ENTER)
                    time.sleep(0.5)
                """attachment_box = driver.find_element_by_xpath('//div[@title = "Anexar"]')
                attachment_box.click()
                image_box = driver.find_element_by_xpath('//input[@accept="*"]')
                image_box.send_keys(filepath)
                time.sleep(1.5)
                driver.find_element_by_xpath('//span[@data-icon="send"]').click()
                time.sleep(1)"""
        time.sleep(10)


driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(999)
driver.get('https://web.whatsapp.com')
input('Pressione enter após fazer login via código qr...\n')
time.sleep(1)



# O parâmetro 2 é a área que você quer contatar. ALTERAR APENAS AQUI. DEVE SER PASSADO COMO STRING
# se especificar "TODOS", todos os contatos serão contatados, o mesmo acontece se passar None ou ""
# se especificar "teste", apenas a pessoa configurada na função receberá a mensagem
contatafreelas(driver, nome=" peda ")
#atualizaDB()