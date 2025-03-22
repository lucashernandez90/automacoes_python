import time
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#----------------------------------------------------------------------Inicializa o WebDriver--------------------------------------------------#
def function_login(email, password):
 
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    driver.maximize_window()
    driver.get(config.URL_SITE)
    

    wait.until(EC.visibility_of_element_located(config.PLACE_HOLDER_USERNAME)).send_keys(config.EMAIL)
    wait.until(EC.visibility_of_element_located(config.PLACE_HOLDER_PASSWORD)).send_keys(config.PASSWORD)

    wait.until(EC.element_to_be_clickable(config.LOGIN_BUTTON)).click()

    time.sleep(5)

    return driver, wait

#-------------------------------------------------------------Clica nos Cards especificos-------------------------------------------------#

def function_click_card(driver, wait, index):  

    try:
        button_cards = wait.until(EC.presence_of_all_elements_located(config.BUTTON_PRODUCTS))
        
        if index < len(button_cards):
            button_cards[index].click()
            print(f"Botao do card {index + 1} clicado")
        else:
            print(f"Erro: Indice {index} fora do alcance")

    except TimeoutException:
        print("O elemento mochila nao foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return driver


#-----------------------------------------------------------Clica no botao de adicionar no carrinho---------------------------------------------#

def function_add_button(driver, wait):

    try:
        button_add_cart = wait.until(EC.element_to_be_clickable(config.BUTTON_ADD_CART))
        button_add_cart.click()
        print("Botao de adicionar no carinho")
        time.sleep(5)
    except TimeoutException:
        print("O elemento de adiconar ao carrinho nao foi achado")
    except Exception as e:
        print(f"Ocorreu um erro:{e}")

    return driver

#-----------------------------------------------------------------------Clica no botao de voltar---------------------------------------------------------# 

def function_back_button(driver, wait):

    try:
        button_back = wait.until(EC.element_to_be_clickable(config.BUTTON_GO_BACK))
        button_back.click()
        print("Botao de voltar para a pagina inicial clicado")
        time.sleep(5)
    except TimeoutException:
        print("O elemento de voltar nao foi achado")
    except Exception as e:
        print(f"Ocorreu um erro:{e}")

    return driver

#------------------------------------------------------------Clica nos ultimos produtos que tenham a opcao de adicionar-----------------------------------------------------------------------------#

def functions_add_cards(driver, wait):

    try:
        buttons_add_cart = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Add to cart']")))
        
        #Procura todos os primeiros botoes que tem o card para adicionar
        if len(buttons_add_cart) >= 4:
            for i in range(4): 
                buttons_add_cart[i].click()
                print(f"Botao {i + 1} clicado para adicionar ao carrinho")
                time.sleep(2)
        else:
            print(f"Erro: Apenas {len(buttons_add_cart)} botoes foram encontrados, e pelo menos 3 são necessários")

    except TimeoutException:
        print("Os botoes de adicionar ao carrinho nao foram encontrados")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    time.sleep(5)

    return driver

#-------------------------------------------------------------------------------Remove os produtos-------------------------------------------------------------------------#

def function_remove(driver, wait):
        
    try:
        button_remove_cart = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Remove']")))

        #Clica nos botoes que tem o botao de remover 
        if len(button_remove_cart) >= 2:
            for i in range(2):
                button_remove_cart[i].click()
                print(f"Botao {i + 1} clicado para remover ao carrinho")
                time.sleep(2)

        else:
            print(f"Erro: Apenas {len(button_remove_cart)} botoes foram encontrados, e pelo menos 2 sao necessarios")
    except TimeoutException:
        print("Os botoes de remover ao carrinho não foram esncontrados")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return driver


#-----------------------------------------------------------Clica em 2 botoes especificios para remover a compra -----------------------------------------------------------------------#

def function_remove_specific(driver, wait):

    try:
        #Aguarda a presença de todos os botões "Remove"
        button_remove_cart = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Remove']")))

        indices = [2, 3]

        for index in indices:
            if index < len(button_remove_cart):  #verifica se o indice esta dentro do limite
                button_remove_cart[index].click()
                print(f"Botao do produto {index + 1} clicado para remover do carrinho")
                time.sleep(2)
            else:
                print(f"Erro: Indice {index} fora do alcance, apenas {len(button_remove_cart)} botoes encontrados.")

    except TimeoutException:
        print("Os botoes de remover ao carrinho não foram encontrados")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    time.sleep(5)

    return driver

#-----------------------------------------------------------Clica no botao do filtro A-Z -------------------------------------------------------------------------------#

def function_filter(driver, wait):

    try:
        button_filter = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class= 'product_sort_container']")))
        button_filter.click()
        print("Botao do filtro foi clicado")

    except TimeoutException:
        print("O botao de filtro nao foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro {e}")

    time.sleep(5)
    
    try:
        click_options_1 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//option[@text()= 'Name (A to Z)']")))
        click_options_1.click()

    except TimeoutException:
        print("Os botoes de filtragem nao foram encontrados")
    except Exception as e:
        print(f"Ocorreu um erro {e}")

    time.sleep(5)

    return driver


#-----------------------------------------------------------Clica no botao Hamburguer ------------------------------------------------------------------------------------------#

def function_hamburguer(driver, wait):

    try:    
        button_hamburguer = wait.until(EC.presence_of_element_located((config.BUTTON_HAMBUGUER)))
        button_hamburguer.click()
        print("Clicou no botao hamburguer")

    except TimeoutException:
        print("O botao hamburguer nao foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    time.sleep(5)

    return driver

#-----------------------------------------------------------Clica no botao Reset dentro do botao Hamburguer-----------------------------------------------------------------------#

def function_reset_button(driver, wait):
    try:    
        item_reset_app = wait.until(EC.presence_of_all_elements_located((config.BUTTON_RESET)))
        item_reset_app[3].click()  
        print("Clicou no botao Reset")
        
        time.sleep(5)
        
    except TimeoutException:
        print("O botao de reset nao foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro: {e}") 

    return driver

#-----------------------------------------------------------Clica no botao X para sair da sessao aonde esta o botao reset ou outros-----------------------------------------------------------------------#

def function_X_button(driver, wait):
    
    try:
        button_x = wait.until(EC.presence_of_element_located((config.BUTTON_X)))
        button_x.click()
        time.sleep(2)

    except TimeoutException:
        print("O botao X nao foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

        time.sleep(10)

    return driver

#-----------------------------------------------------------------------------Funcao para clicar no botao do carrinho---------------------------------------------------#

def function_cart_button(driver,wait):

    try:
        button_cart = wait.until(EC.presence_of_element_located((config.BUTTON_CART)))
        print("botao do carrinho encontrado")
        button_cart.click()
        time.sleep(5)

    except TimeoutException:
        print("O botao do carrinho nao foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
        time.sleep(10)

    try:
        button_checkout = wait.until(EC.presence_of_element_located((config.BUTTON_CHECKOUT)))
        print("botao checkout encontrado")
        button_checkout.click()
    except TimeoutException:
        print("O botao checkout nao foi achado")
    except Exception as e:
        print(f"Ocorreu um erro {e}")

        time.sleep(5)

    try:
        wait.until(EC.visibility_of_element_located(config.PLACE_HOLDER_FIRST_NAME)).send_keys(config.FIRT_NAME)
        wait.until(EC.visibility_of_element_located(config.PLACE_HOLDER_LAST_NAME)).send_keys(config.LAST_NAME)
        wait.until(EC.visibility_of_element_located(config.PLACE_HOLDER_POSTAL_CODE)).send_keys(config.POSTAL_CODE)

        print("O processo de cadastro foi completo")

    except TimeoutException:
        print("O processo de preencher o usuario nao deu certo")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

        time.sleep(5)

    try:
        wait.until(EC.element_to_be_clickable(config.BUTTON_CONTINUE_SHOP)).click()
        print(f"Clicou no botao de continue: {config.BUTTON_CONTINUE_SHOP}")

        wait.until(EC.element_to_be_clickable(config.BUTTON_FINISH_CART)).click()
        print(f"Clicou no botao de finalizar a compra: {config.BUTTON_FINISH_CART}")
        time.sleep(5)

        wait.until(EC.element_to_be_clickable(config.BUTTON_BACK_HOME)).click()
        print(f"Clicou no botao de voltar para a pagina inicial: {config.BUTTON_BACK_HOME}")

    except TimeoutException:
        print("Nao conseguiu terminar o processo da compra")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

        time.sleep(5)

    return driver

#----------------------------------------------------------------------------------Funcao que clica no botao das rede sociais--------------------------------------------------------#


def function_buttons_social(driver, wait):
    
    button_twitter = wait.until(EC.presence_of_element_located((config.BUTTON_TWITTER)))
    print("Achou o botao do twitter")
    button_twitter.click()

    time.sleep(2)

    button_facebook = wait.until(EC.presence_of_element_located((config.BUTTON_FACEBOOK)))
    print("Achou o botao do facebook")
    button_facebook.click()

    time.sleep(2)

    button_linkedin = wait.until(EC.presence_of_element_located((config.BUTTON_LINKEDIN)))
    print("Achou o botao do linkedin")
    button_linkedin.click()

    time.sleep(20)
     
    try:
        button_sign_in_linkedin = wait.until(EC.presence_of_element_located((config.BUTTON_SIGN_IN)))
        print("Achou o botao de entrar no linkedin")
        button_sign_in_linkedin.click()
    except TimeoutException:
        print("Nao achou o botao de entrar no linkedin")
    except Exception as e:
        print(f"Ocorreu um erro {e}")

        wait.until(EC.visibility_of_element_located((config.PLACE_HOLDER_LINKEDIN_USERNAME))).send_keys(config.LINKEDIN_EMAIL)
        print("Preenchou com o email do linkedin")
                
        time.sleep(10)

        wait.until(EC.visibility_of_element_located((config.PLACE_HOLDER_LINKEDIN_PASSWORD))).send_keys(config.LINKEDIN_PASSWORD)
        print("Preenchou a senha do linkedin")

        time.sleep(10)

    return driver

