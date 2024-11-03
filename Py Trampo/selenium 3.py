from selenium import webdriver
from selenium.webdriver.commom.by import by
from selenium.webdriver.commom.keys import Keys
from selenium.webdriver.chrome.options import Options

import time
import easygui
import os

from tqdm import tqdm

def xpath(browser,caminho):
    return browser.find_element_by_xpath(caminho)



def wait(segundos):
    for i in tqdm(range(segundos)):
        time.sleep(1)


        options = Options()
        prefs = {"download.default_directory": r"C:\Users\vinicius.domingues\Documents\\"
                 }
        options.add_experimental_option("prefs",prefs)


        try:
            os.remove(r"C:\Users\vinicius.domingues\Documents\OTD.xlsx")
        except:
                pass


browser = webdriver.Chrome(exacutable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe", options=options)

sap_url = "https://by-dcs1p.bayer.cnb:44305/sap/bc/ui2/flp?sap-client=300#ZTOD-display?sap-appvar-id=customer.bayer.zlogistic&/?sap-iapp-state=ASU3RSLQCOL746PHUFIODMSSMUV488ONOTAB69OU&sap-iapp-state--history=TASLU7NPY32DTMRQ0LDN32GR9FR6IZUMYJIPL69SS"

browser.get(sap_url)

wait(25)

selecionar_menu = browser.find_element_by_xpath('//[@aria-label="Open menu"]')
selecionar_menu.click()

wait(2)

selecionar_exportar =  browser.find_element_by_xpath('//div[contais(text(),"Exportar como...")]')
selecionar_exportar.click()

wait(2)

clicar_texto = browser.find_element_by_xpath('//*[@value="Deliveries"]')
clicar_texto.click()
clicar_texto.send_keys(Keys.CONTROL,'a')
clicar_texto.send_keys('OTD')

wait(2)

checkbox =  browser.find_element_by_xpath('//[@aria-label="Dividir células com varios valores"]')
clicar_texto.click()

for i in range(1):
    botao_exportar = xpath(browser,'//bdi[contains(text(),"Exportar")]')
    botao_exportar.click()
    wait(3)

while not os.path.exists(r"C:\Users\vinicius.domingues\Documents\OTD.xlsx"):
    time.sleep(10)
    print("Aguardando Arquivo OTD")

    import os
    os.starfile(r'C:\Users\vinicius.domingues\Documents\Tracking.bat')
