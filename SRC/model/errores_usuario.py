class ErrorNoEmail(Exception):
    def __init__(self):
        super().__init__("Agregue un email para registrarse")

class ErrorContraseñaCorta(Exception):
    def __init__(self):
        super().__init__("Agregue una contraseña de minimo 8 caracteres")

class ErrorEmailYa(Exception):
    def __init__(self):
        super().__init__("Este email ya ha sido registrado")

class ErrorContraseñaIncorrecta(Exception):
    def __init__(self):
        super().__init__("Contraseña Incorrecta")

class ErrorEmailNo(Exception):
    def __init__(self):
        super().__init__("Este email no ha sido registrado")

class ErrorContraseñaAnteriorIn(Exception):
    def __init__(self):
        super().__init__("Su contraseña anterior es incorrecta")

class ErrorContraseñaNoCoincide(Exception):
    def __init__(self):
        super().__init__("Las contraseñas no coinciden")
