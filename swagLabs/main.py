import time
import config
import functions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


if __name__ == "__main__":

    #Abre o navegador e realiza o login
    driver, wait = functions.function_login(config.EMAIL, config.PASSWORD)
    
    #Faz o processo do primeiro Card
    driver = functions.function_click_card(driver, wait, 0)
    driver = functions.function_add_button(driver, wait)
    driver = functions.function_back_button(driver, wait)

    #Faz o processo do segundo Card
    driver = functions.function_click_card(driver, wait, 1)
    driver = functions.function_add_button(driver, wait)
    driver = functions.function_back_button(driver, wait)

    #Adiciona os quatro ultimos produtos
    driver = functions.functions_add_cards(driver, wait)

    #Remove dois produtos
    driver = functions.function_remove(driver, wait)
    #Remove dois produtos especificos
    driver = functions.function_remove_specific(driver, wait)

    #Clica no botao de filtro e clica nos botoes de filtro
    #driver = functions.function_filter(driver, wait)  (nao consertei ainda)

    #Clica no botao hamburguer
    driver = functions.function_hamburguer(driver, wait)
    #Clica no botao Reset 
    driver = functions.function_reset_button(driver, wait)
    #Clica no botao X para sair da sessao dentro do botao hamburguer
    driver = functions.function_X_button(driver, wait)

    #Clica no botao do carrinho + termina a compra
    driver = functions.function_cart_button(driver, wait)

    #Clica nos botoes das redes sociais + entra na conta do linkedin(tenho que consertar --> problema no botao de entrar do linkedin)
    driver = functions.function_buttons_social(driver, wait) 
    
driver.quit()