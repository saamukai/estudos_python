import time
import os
from newCRUD import CRUD
from selenium import webdriver as web
from selenium.common.exceptions import NoSuchElementException as NotFound
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class FreelancerBot:
    def __init__(self,name='ALL',msg='mensagem.txt') -> None:
        
        self.msg = msg
        self.sendMessage(self.startBot(),name)
    
    def startBot(self,url:str='https://web.whatsapp.com',chrome:str='chromedriver.exe')->None:
        driver = web.Chrome(chrome)
        driver.get(url)
        driver.implicitly_wait(999)
        input('Pressione enter após fazer login via código qr...\n')
        time.sleep(1)
        return driver

    def sendMessage(self,driver,name):
        contacts = self.queryDB(name)
        for number,name in contacts:
            number = str(number).replace('-', '').replace(' ', '')
            print(f"Enviando mensagem para {str(name).title()} ({number})")
            # number = '5598985653456'
            driver.get(f"https://web.whatsapp.com/send?phone={number}&source=&data=#")
            self.readMessage(driver,'mensagem.txt',name)

    def readMessage(self,driver:web,reader:str,name:str):
        # time.sleep(3)
        driver = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[1]/div/div[2]")
        time.sleep(1.5)
        driver.send_keys(f"Olá {str(name).title()}, você teria interesse de fazer um trabalho de freelancer?")
        driver.send_keys(Keys.ENTER)
        with open(reader, "r", encoding="utf-8") as message:
            for line in message:
                    driver.send_keys(str(line).strip())
                    driver.send_keys(Keys.ENTER)
                    time.sleep(0.5)

    def sendDocFile(self):
        pass

    def queryDB(self,name):

        if name in  ['ALL','',None]:
            data = CRUD.Search('SELECT Number,Name FROM freelancers')
        else:
            data = CRUD.Search("SELECT Number,Name FROM freelancers WHERE Name=?",str(name).strip())
        return data


        
if __name__ == '__main__':
    bot = FreelancerBot()

