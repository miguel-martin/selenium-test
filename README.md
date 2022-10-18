# Test selenium

  Prueba de selenium: hacer login en Zaguan (redirige a SIR-IdP)

## Instalación

  Crear venv y activarlo:

    $ python3 -m venv venv; source venv/bin/activate

  Instalar requisitios:

    $ pip install -r requirements.txt

  Ejemplo programación imperativa: Modificar el fichero `test-zaguan-login.py` para proporcionar credenciales correctos...

    test_username = ...
    test_password = ...
  
  Ejemplo programación orientada a objetos: Modificar el fichero `ZaguanValidator.py`para proporcionar credenciales correctos...

    # User data
    USERNAME = "512798"
    PASSWORD = "AQUI_EL_PASSWORD"
    CADENA_PARA_COMPROBAR_QUE_LOGIN_OK = "Miguelm"


## Uso

  Ejemplo programacion imperativa: 

    $ python3 test-zaguan-login.py

  Ejemplo programación orientada a objetos:

    $ python3 ZaguanValidator.py