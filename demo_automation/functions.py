import time
import config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

#---------------------------------------------------------Funcao para de Inicializacao---------------------------------------------------------------#

def inicialize_button():
    driver.maximize_window()
    driver.get(config.URL_SITE)

    wait.until(EC.visibility_of_element_located(config.PLACE_HOLDER_EMAIL_SIGN_UP)).send_keys(config.EMAIL)
    wait.until(EC.visibility_of_element_located(config.IMAGE_SING_UP)).click()
    print("Preencheu a caixa de email")

#---------------------------------------------------------Funcao de preenchimento de cadastro---------------------------------------------------------------#

def sign_up_function():

    driver.delete_all_cookies()
    print("Cookies deletados!")

    # Verifica se ainda há cookies
    cookies = driver.get_cookies()
    print("Cookies restantes:", cookies)

    wait.until(EC.visibility_of_element_located(config.PLACE_HOLDER_FIRST_NAME)).send_keys(config.FIRST_NAME)
    print("Preencheu a caixa do primeiro nome")
    wait.until(EC.visibility_of_element_located(config.PLACE_HOLDER_LAST_NAME)).send_keys(config.LAST_NAME)
    print("Preencheu a caixa do sobrenome")

    time.sleep(2)

    wait.until(EC.visibility_of_element_located(config.FILL_TEXT_ADDRESS)).send_keys(config.ADDRESS)
    print("Preencheu a caixa do endereço")
    wait.until(EC.visibility_of_element_located(config.EMAIL_ADDRESS_REGISTER)).send_keys(config.EMAIL)
    print("Preencheu a caixa do email")

    time.sleep(2)

    wait.until(EC.visibility_of_element_located(config.FILL_TEXT_PHONE)).send_keys(config.PHONE) #Preenchimento da caixa de texto do telefone 
    print("preencheu a caixa de texto do telefone")

    wait.until(EC.visibility_of_element_located(config.RADIO_BUTTON_MALE)).click() #Clique no radiobutton do genero
    print("Clicou no botao da opcao Male do radio button")

    hobbies_checkboxes = wait.until(EC.visibility_of_all_elements_located(config.CHECK_BUTTONS_HOBBIES))

    for checkbox in hobbies_checkboxes:
        checkbox.click()

    time.sleep(2)

    wait.until(EC.visibility_of_element_located(config.CLICK_LANGUAGES)).click() #Clica no botao das linguas
    print("Clicou no botao para selecionar as linguas")
    wait.until(EC.visibility_of_all_elements_located(config.SELECT_LANGUAGES)) 

    time.sleep(5)
    
    linguas = driver.find_elements(*config.SELECT_LANGUAGES)
    indices_desejados = [0, 5, 8, 9] #indice das linguas especificas que eu quero

    for i in indices_desejados:
        if i < len(linguas):  #Garante que o índice está dentro da lista
            linguas[i].click()
            print(f"Clicou no idioma com o índice {i}")

    time.sleep(5)

    action = ActionChains(driver)
    action.move_by_offset(100, 100).click().perform()

    wait.until(EC.visibility_of_element_located(config.SELECT_SKILLS)).click() #Clica no botao das suas habilidades 
    print("clicou no botao Skills")
    wait.until(EC.visibility_of_element_located(config.SELECT_SKILLS_OPTIONS)).click() #Seleciona qual habilidade voce quer
    print("Escolheu uma habilidade")

    time.sleep(2)

    action.move_by_offset(100, 100).click().perform()

    wait.until(EC.visibility_of_element_located(config.SELECT_COUNTRY)).click()
    wait.until(EC.visibility_of_all_elements_located(config.SELECT_OPTIONS_COUNTRY))

    countrys = driver.find_elements(*config.SELECT_OPTIONS_COUNTRY)
    indice_countrys = [5]

    for i in indice_countrys:
        if i < len(countrys):
            countrys[i].click()
            print(f"Clicou no pais que queria {i}")

    time.sleep(5)

    wait.until(EC.visibility_of_element_located(config.SELECT_DAY_OF_BIRTH)).click()
    wait.until(EC.visibility_of_element_located(config.CLICK_DAY_OF_BIRTH)).click()

    wait.until(EC.visibility_of_element_located(config.SELECT_MONTH_OF_BIRTH)).click()
    wait.until(EC.visibility_of_element_located(config.CLICK_MONTH_OF_BIRTH)).click()

    year_birth = wait.until(EC.presence_of_element_located(config.SELECT_YEAR_OF_BIRTH))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", year_birth)
    time.sleep(1)
    year_birth.click()

    wait.until(EC.visibility_of_element_located(config.SELECT_YEAR_OF_BIRTH )).click()
    wait.until(EC.visibility_of_element_located(config.CLICK_YEAR_OF_BIRTH)).click()

    time.sleep(2)

    wait.until(EC.visibility_of_element_located(config.FILL_PASSWORD)).send_keys(config.PASSWORD)
    wait.until(EC.visibility_of_element_located(config.FILL_CONFIRM_PASSWORD)).send_keys(config.PASSWORD)

    time.sleep(5)

    wait.until(EC.visibility_of_element_located(config.CHOSE_BUTTON_FILE)).click()
    wait.until(EC.visibility_of_element_located(config.SUBMIT_BUTTON)).click()
    