from abc import ABC, abstractmethod

class ServiceValidator(ABC):

    def __init__(self, isLoggedIn: bool=False) -> None:
        super().__init__()
        self.isLoggedIn = False

    @property
    def isLoggedIn(self) -> bool:
        return  self._isLoggedIn

    @isLoggedIn.setter
    def isLoggedIn(self, value:bool):
        self._isLoggedIn = value

    @abstractmethod
    def login(self, url: str, username: str, password: str) -> bool: 
        """ Prueba el login de la aplicacion contra url usando username/password"""

    @abstractmethod
    def logout(self, url: str) -> bool:
        """ Prueba el logout de la aplicacion contra url """

    def run_test(self, expected_result: bool, func, *args) -> bool:
        """ Realiza un test. 
            expected_result: el resultado esperado del test (True o False)
            funct: funcion a ejecutar
            *args: argumentos a pasarle
        """
        print("RUNNING TEST: '{}'".format(func.__name__))
        try:
            if (func(*args) == expected_result):
                print(" [OK]\n")
                return True
            else:
                print(" [ERROR]\n")
                return False
        except Exception as err:
            print(" [ERROR]: {}".format(err))
            return False