from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDriver():

    MAX_WAIT_TIME=30 # max time to wait for response

    def __init__(self) -> None:
        # setup
        options = Options()
        options.add_argument("start-maximized")
        #options.add_argument("--disable-extensions")
        #options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_argument('--no-sandbox') 
        options.add_argument(f'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

        try:
            self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        except Exception as err:
            print("ERROR: {0}".format(err))
            print("¿Esta instalado el binario de Chrome?")
            self._driver = None

    @property 
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, value):
        self._driver = value

    def find_by_id(self, value):
        return self._driver.find_element(By.ID, value)

    def find_by_xpath(self, value):
        return self._driver.find_element(By.XPATH, value)
    
    def find_by_classname(self, value):
        return self._driver.find_element(By.CLASS_NAME, value)

    def get(self, value):
        return self._driver.get(value)

    def page_source(self) -> str:
        """ Returns page source """
        return self._driver.page_source
    
    def wait_until_class_name_is_present(self, value, max_time=MAX_WAIT_TIME):
        WebDriverWait(self._driver,max_time).until(EC.presence_of_element_located((By.CLASS_NAME, value)))