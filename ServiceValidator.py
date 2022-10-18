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