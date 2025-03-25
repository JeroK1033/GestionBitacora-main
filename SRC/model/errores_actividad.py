class ErrorDescripcion(Exception):
    def __init__(self,):
        super().__init__(f"La descripción no puede estar vacía")
        
class ErrorFechaHora(Exception):
    def __init__(self,):
        super().__init__(f"La fecha y hora no pueden estar vacías")
    
class ErrorFechaHoraInvalida(Exception):
    def __init__(self):
        super().__init__("La fecha y la hora son invalidas")

class ErrorNoFechas(Exception):
    def __init__(self):
        super().__init__("Agregue una fecha")

class ErrorFechaInvalida(Exception):
    def __init__(self):
        super().__init__("Las fechas agregadas no son compatibles")

class ErrorSesionNoIniciada(Exception):
    def __init__(self):
        super().__init__("Para hacer esto, primero inicie sesion")

class ErrorNoAnexos(Exception):
    def __init__(self):
        super().__init__("Agregue al menos un anexo")