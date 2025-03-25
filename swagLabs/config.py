from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#-----------------------------------------------------------------------Variaveis----------------------------------------------------------#
URL_SITE = 'https://www.saucedemo.com/'
EMAIL = 'standard_user'
PASSWORD = 'secret_sauce'

FIRT_NAME = 'Lucas'
LAST_NAME = 'Hernandez'
POSTAL_CODE = '02032490-29'

LINKEDIN_EMAIL = 'lucasohernandez89@gmail.com'
LINKEDIN_PASSWORD = 'Ak57@24hjlm9'

#-----------------------------------------------------------------------Localizadores-------------------------------------------------------#
PLACE_HOLDER_USERNAME = (By.XPATH, "//input[@placeholder='Username']")
PLACE_HOLDER_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
LOGIN_BUTTON = (By.XPATH, "//input[@id= 'login-button']")
BUTTON_PRODUCTS = (By.XPATH, "//div[@class= 'inventory_item_name ']")
BUTTON_ADD_CART = (By.XPATH, "//button[@class= 'btn btn_primary btn_small btn_inventory']")
BUTTON_GO_BACK = (By.XPATH, "//button[@class= 'btn btn_secondary back btn_large inventory_details_back_button']")

# BUTTON_ADD = (By.XPATH, "//button[text()='Add to cart']")
# BUTTON_REMOVE = (By.XPATH, "//button[text()='Remove')
# BUTTON_FILTER = (By.XPATH, "//span[@class= 'product_sort_container']")

BUTTON_HAMBUGUER = (By.XPATH, "//button[@id= 'react-burger-menu-btn']")
BUTTON_RESET = (By.XPATH, "//a[@class= 'bm-item menu-item']")
BUTTON_X = (By.XPATH, "//button[@id= 'react-burger-cross-btn']")
BUTTON_CART = (By.XPATH, "//a[@class= 'shopping_cart_link']")

BUTTON_CHECKOUT = (By.XPATH, "//button[@class= 'btn btn_action btn_medium checkout_button ']")
BUTTON_CONTINUE_SHOP = (By.XPATH, "//input[@class= 'submit-button btn btn_primary cart_button btn_action']")

PLACE_HOLDER_FIRST_NAME = (By.XPATH, "//input[@placeholder= 'First Name']")
PLACE_HOLDER_LAST_NAME = (By.XPATH, "//input[@placeholder= 'Last Name']")
PLACE_HOLDER_POSTAL_CODE = (By.XPATH, "//input[@placeholder= 'Zip/Postal Code']")

BUTTON_FINISH_CART = (By.XPATH, "//button[@class= 'btn btn_action btn_medium cart_button']")
BUTTON_BACK_HOME = (By.XPATH, "//button[@class= 'btn btn_primary btn_small']")

BUTTON_TWITTER = (By.XPATH, "//li[@class= 'social_twitter']")
BUTTON_LINKEDIN = (By.XPATH, "//li[@class= 'social_linkedin']")
BUTTON_FACEBOOK = (By.XPATH, "//li[@class= 'social_facebook']")

BUTTON_SIGN_IN = (By.XPATH, "//div[@class= 'sign-in-modal__outlet-btn cursor-pointer btn-md btn-primary btn-secondary']")
PLACE_HOLDER_LINKEDIN_USERNAME = (By.XPATH, "//autocomplete[@id= 'username']")
PLACE_HOLDER_LINKEDIN_PASSWORD = (By.XPATH, "//autocomplete[@id= 'current-password']")