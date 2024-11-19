from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path='C:\\Users\\vinicius.domingues\\Documents\\chromedriver-win64\\chromedriver.exe')

try:

    driver.get('https://bayeroutbound.brasilrisk.com.br/Login/Logout')


    time.sleep(3)

 
    usuario_input = driver.find_element(By.NAME, 'Usuario') 
    usuario_input.send_keys('')#Nome de Usuario

   
    senha_input = driver.find_element(By.NAME, 'Senha')
    senha_input.send_keys('')#Senha

 
    botao_login = driver.find_element(By.XPATH, '//button[contains(text(), "Entrar")]') 
    botao_login.click()


    time.sleep(5)

finally:

    driver.quit()
