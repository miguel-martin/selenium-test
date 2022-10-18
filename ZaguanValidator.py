from SeleniumDriver import SeleniumDriver
from ServiceValidator import ServiceValidator

class ZaguanValidator(ServiceValidator):

    # Zaguan data
    LOGIN_URL = "https://zaguan.unizar.es/youraccount/login?ln=es&referer=https%3A//zaguan.unizar.es/%3F"
    LOGOUT_URL = "https://sir.unizar.es/simplesamlphp/saml2/idp/SingleLogoutService.php?ReturnTo=https://zaguan.unizar.es"
    ZAGUAN_LOGIN_INFO_CLASS = 'userinfo'

    # IdP data: sir.unizar.es form id's
    USERNAME_FORM_ID = "username" 
    PASSWORD_FORM_ID = "password"
    SUBMIT_XBUTTON_PATH = '//*[@id="login"]/input[3]'

    # User data
    USERNAME = "512798"
    PASSWORD = "AQUI_EL_PASSWORD"
    CADENA_PARA_COMPROBAR_QUE_LOGIN_OK = "Miguelm"

    def __init__(self, isLoggedIn: bool=False) -> None:
        super().__init__()
        self.isLoggedIn = False

    def login(self, url = LOGIN_URL, username = USERNAME, password = PASSWORD) -> bool: 
        """ Prueba el login de la aplicacion """

        print("Comprobando login ZAGUAN")

        # create Selenium Driver...
        driver = SeleniumDriver()

        # go to login url
        driver.get(url)

        # fill login form
        un = driver.find_by_id(self.USERNAME_FORM_ID)
        pw = driver.find_by_id(self.PASSWORD_FORM_ID)

        # send keys
        un.send_keys(username)
        pw.send_keys(password)

        try:
            driver.find_by_xpath(self.SUBMIT_XBUTTON_PATH).click()
             # put some delay here, WebDriverWait or time.sleep()
            driver.wait_until_class_name_is_present(self.ZAGUAN_LOGIN_INFO_CLASS)
           
            #print(driver.title)

            loggedin_user = driver.find_by_classname(self.ZAGUAN_LOGIN_INFO_CLASS).text
            assert (loggedin_user == self.CADENA_PARA_COMPROBAR_QUE_LOGIN_OK)
            print('Login correcto :)')
            return True
        except Exception as err:
            #print("ERROR: {0}".format(err))
            print("Login incorrecto :(")

        return False

    def logout(self, url: str) -> bool:
        """ Prueba el logout de la aplicacion """
        print("Comprobando servicio logout ZAGUAN")
        return True

print("Validador del servicio ZAGUAN")

validador = ZaguanValidator()
if (validador.login()):
    print("Login Zaguan ok")
else:
    print("Login Zaguan not ok")