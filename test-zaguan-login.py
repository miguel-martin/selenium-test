#!./venv/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# --- config ----

# url de login a comprobar (debe redirigir a SIR)
url = 'https://zaguan.unizar.es/youraccount/login?ln=es&referer=https%3A//zaguan.unizar.es/%3F'
zaguan_login_info_class = 'userinfo'

# datos de usuario de prueba
test_username = "512798"
test_password = "AQUI_EL_PASS"
cadena_para_comprobar_que_login_ok = "Miguelm"

# sir.unizar.es form id's
username_form_id = "username" 
password_form_id = "password"
submit_button_xpath = '//*[@id="login"]/input[3]'
# ---------------

# setup
options = Options()
options.add_argument("start-maximized")

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
except Exception as err:
    print("ERROR: {0}".format(err))
    print("¿Esta instalado el binario de Chrome?")
    quit()

# run
driver.get(url)

# fill form
username = driver.find_element(By.ID, username_form_id)
password = driver.find_element(By.ID, password_form_id)

username.send_keys(test_username)
password.send_keys(test_password)


try:
    driver.find_element(By.XPATH, submit_button_xpath).click()
    # put some delay here, WebDriverWait or time.sleep()

    loggedin_user = driver.find_element(By.CLASS_NAME, zaguan_login_info_class).text
    assert (loggedin_user == cadena_para_comprobar_que_login_ok)
    print('Login correcto :)')
except:
    print('Login incorrecto :(')


