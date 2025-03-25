import datetime

class Supervisor:
    def __init__(self, nombre: str, correo: str, contraseña: str):
        self.contraseña = contraseña
        self.correo = correo
        self.nombre = nombre
    
    def cambiar_contraseña(self)->str:
        pass
    
    def iniciar_sesion(self):
        pass
    
class Reporte:
    def __init__(self, idreporte: int, rangofecha: datetime, contenido: str):
        self.contenido = contenido
        self.rangoFecha = rangofecha
        self.idReporte = idreporte
    
    def generar_reporte(self):
        pass