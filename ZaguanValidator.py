from unittest.mock import NonCallableMagicMock
from SeleniumDriver import SeleniumDriver
from ServiceValidator import ServiceValidator

class ZaguanValidator(ServiceValidator):

    ################### CONFIGURACION DEL VALIDADOR PARA EL SERVICIO ##########

    # Zaguan data
    HOME = 'https://zaguan.unizar.es/?ln=es'
    LOGIN_URL = "https://zaguan.unizar.es/youraccount/login?ln=es&referer=https%3A//zaguan.unizar.es/%3F"
    LOGOUT_URL = "https://sir.unizar.es/simplesamlphp/saml2/idp/SingleLogoutService.php?ReturnTo=https://zaguan.unizar.es"
    ZAGUAN_LOGIN_INFO_CLASS = "userinfo"
    ZAGUAN_HOME_CLASS = "home"

    # IdP data: sir.unizar.es form id's
    USERNAME_FORM_ID = "username" 
    PASSWORD_FORM_ID = "password"
    SUBMIT_XBUTTON_PATH = '//*[@id="login"]/input[3]'

    # User data
    USERNAME = "512798"
    PASSWORD = "AQUI_EL_PASSWORD"
    CADENA_PARA_COMPROBAR_QUE_LOGIN_OK = "Miguelm"

    # Max wait time
    MAX_WAIT_TIME = 3 # 3seg

    ###########################################################################

    def __init__(self, isLoggedIn: bool=False) -> None:
        super().__init__()
        self.isLoggedIn = False
        self.create_driver()

    def create_driver(self):
        self.driver = SeleniumDriver()
    
    def destroy_driver(self):
        self.driver = None

    def login(self, url = LOGIN_URL, username = USERNAME, password = PASSWORD) -> bool: 
        """ Prueba el login de la aplicacion """

        #print("Log in ZAGUAN")

        # go to login url
        self.driver.get(url)

        # fill login form
        un = self.driver.find_by_id(self.USERNAME_FORM_ID)
        pw = self.driver.find_by_id(self.PASSWORD_FORM_ID)

        # send keys
        un.send_keys(username)
        pw.send_keys(password)

        try:
            self.driver.find_by_xpath(self.SUBMIT_XBUTTON_PATH).click()
             # put some delay here, WebDriverWait or time.sleep()
            self.driver.wait_until_class_name_is_present(self.ZAGUAN_LOGIN_INFO_CLASS, self.MAX_WAIT_TIME)

            loggedin_user = self.driver.find_by_classname(self.ZAGUAN_LOGIN_INFO_CLASS).text
            assert (loggedin_user == self.CADENA_PARA_COMPROBAR_QUE_LOGIN_OK)
            self.isLoggedIn=True
            #print('Login correcto :)')
            return True

        except Exception as err:
            print("ERROR: {0}".format(err))
            #print("Login incorrecto :(")

        return False


    def logout(self, url=LOGOUT_URL) -> bool:
        """ Hace logout de la aplicacion """

        #print("Log out ZAGUAN")
        if (self.isLoggedIn):
            self.driver.get(self.LOGOUT_URL) # visit LogoutUrl
            self.driver.wait_until_class_name_is_present(self.ZAGUAN_HOME_CLASS, self.MAX_WAIT_TIME) # wait until returned to home page
        self.isLoggedIn = False
        return True


    def check_text(self, url: str, value: str) -> bool:
        """ Comprueba si existe el texto value en la URL url estando loggeado en la aplicacion """
           
        self.driver.get(url)

        #print("Comprobando si existe el texto '{0}' en {1}".format(value, url))
        if (value in self.driver.page_source()):
            #print("Existe")
            return True

        #print("No existe")
        return False



if __name__ == "__main__":

    print("\nValidador del servicio ZAGUAN\n")
    validador = ZaguanValidator()

    # test: buscar una cadena que solo sale estando loggeado: no debe encontrarse
    validador.run_test(False, validador.check_text, validador.HOME, 'Sus envíos')

    # prueba, hacer login
    validador.run_test(True, validador.login)

    # prueba, buscar una cadena que solo sale estando loggeado
    validador.run_test(True, validador.check_text, validador.HOME, 'Sus envíos')

    # prueba, hacer logout
    validador.run_test(True, validador.logout)

    # test: buscar una cadena que solo sale estando loggeado: no debe encontrarse
    validador.run_test(False, validador.check_text, validador.HOME, 'Sus envíos')

