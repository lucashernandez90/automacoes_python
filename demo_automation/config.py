import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#-------------------------------------------------------------------Variveis----------------------------------------------------------------------------#
URL_SITE = 'https://demo.automationtesting.in/Index.html'
EMAIL = 'a.m.lucashernandez@gmail.com'
PASSWORD = 'senha123'
FIRST_NAME = 'Lucas'
LAST_NAME = 'de Oliveira Hernandez'
ADDRESS = 'Rua Teste 1423'
PHONE = '1196786249'

#-------------------------------------------------------------------Localizadores------------------------------------------------------------------------#

#Placeholder do sing up
PLACE_HOLDER_EMAIL_SIGN_UP = (By.XPATH, "//input[@placeholder='Email id for Sign Up']") 
#Botao de entrar no cadastro
IMAGE_SING_UP = (By.XPATH, "//img[@id='enterimg']")

#Caminho para completar o Primeiro nome
PLACE_HOLDER_FIRST_NAME = (By.XPATH,"//input[@placeholder='First Name']")
#Caminho para completar o Sobrenome
PLACE_HOLDER_LAST_NAME = (By.XPATH,"//input[@placeholder='Last Name']")

#Caminho para completar a caixa de email 
FILL_TEXT_ADDRESS = (By.XPATH, "//textarea[@ng-model='Adress']")
EMAIL_ADDRESS_REGISTER = (By.XPATH,"//input[@ng-model='EmailAdress']") 

#Caminho do preenchimento do email
FILL_TEXT_PHONE = (By.XPATH, "//input[@ng-model='Phone']")

#Caminho do radiobutton genero masculino
RADIO_BUTTON_MALE = (By.XPATH, "//input[@value='Male']")

#Caminho do radiobutton genero feminino
RADIO_BUTTON_FEMALE = (By.XPATH, "//input[@value=' FeMale']")

#Caminho dos checkbutton
CHECK_BUTTONS_HOBBIES = (By.XPATH, "//input[@type='checkbox']")

#Caminho para clicar na box das linguas
CLICK_LANGUAGES = (By.XPATH, "//div[@id='msdd']")
#Caminho para selecionar as linguagens
SELECT_LANGUAGES = (By.XPATH, "//li[@class='ng-scope']")

#Caminho que clica na box das suas habilidades
SELECT_SKILLS = (By.XPATH, "//select[@id='Skills']")
SELECT_SKILLS_OPTIONS = (By.XPATH, "//option[@value='C']")

#Caminho para selecionar os paises
SELECT_COUNTRY = (By.XPATH,"//span[@class='select2-selection select2-selection--single']")
SELECT_OPTIONS_COUNTRY = (By.XPATH,"//li[@class='select2-results__option']")

#Caminho para selecionar o ano do aniversario
SELECT_DAY_OF_BIRTH = (By.XPATH, "//select[@id='yearbox']")
CLICK_DAY_OF_BIRTH = (By.XPATH, "//option[@value='2002']")

#Caminho para selecionar o mes do aniversario
SELECT_MONTH_OF_BIRTH = (By.XPATH, "//select[@ng-model='monthbox']")
CLICK_MONTH_OF_BIRTH = (By.XPATH, "//option[@value='September']")

#Caminho para selecionar o dia do aniversario
SELECT_YEAR_OF_BIRTH = (By.XPATH, "//select[@id='daybox']")
CLICK_YEAR_OF_BIRTH = (By.XPATH, "//option[@value='14']")

#Caminho para preencher a caixa de criacao da senha 
FILL_PASSWORD = (By.XPATH, "//input[@id='firstpassword']")
FILL_CONFIRM_PASSWORD = (By.XPATH, "//input[@id='secondpassword']")

#Caminho para clicar no botao de selecionar um documento no computador
# CHOSE_BUTTON_FILE = (By.XPATH, "//input[@id='imagesrc']")

#Caminho para o botao para se cadastrar
SUBMIT_BUTTON = (By.XPATH, "//button[@id='submitbtn']")