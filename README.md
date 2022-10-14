# Test selenium

  Prueba de selenium: hacer login en Zaguan (redirige a SIR-IdP)

## Instalación

  Crear venv y activarlo:

    $ python3 -m venv venv; source venv/bin/activate

  Instalar requisitios:

    $ pip install -r requirements.txt

  Modificar el fichero `test-zaguan-login.py` para proporcionar credenciales correctos...

    test_username = ...
    test_password = ...

## Uso

  Ejecutar:

    $ python3 test-zaguan-login.py