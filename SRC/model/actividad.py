from SRC.model.errores_actividad import ErrorFechaHoraInvalida, ErrorNoFechas, ErrorFechaInvalida, ErrorDescripcion, ErrorFechaHora, ErrorNoAnexos, ErrorSesionNoIniciada
from SRC.model.supervisor import Supervisor
from datetime import datetime



class Archivo:
    def __init__(self, nombre: str, tipo: str, ruta: str):
        self.Ruta = ruta
        self.Tipo = tipo
        self.Nombre = nombre

    def subir_archivo(self):
        pass

class Actividad:
    
    
    def __init__(self, idactividad: int, fechahora: datetime, responsable: str, descripcion: str, condicionesclimaticas: str, anexos: list[Archivo], supervisor: Supervisor):

        self.fechahora = fechahora
        self.Supervisor = supervisor
        self.Anexos = anexos
        self.CondicionesClimaticas = condicionesclimaticas
        self.Descripcion = descripcion
        self.Responsable = responsable
        self.idActividad = idactividad
        

    def registrar_actividad(self):
        global usuario_actual, actividades
        if not usuario_actual:
            raise ErrorSesionNoIniciada()
        fecha_hora = input("Ingrese la fecha y hora (YYYY-MM-DD HH:MM): ")
        if not fecha_hora:
            raise ErrorFechaHora()
        try:
            fecha_hora = datetime.datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
        except ValueError:
            raise ErrorFechaHoraInvalida()
        
        descripcion = input("Ingrese la descripción de la actividad: ")
        if not descripcion:
            raise ErrorDescripcion()
        
        responsable = input("Ingrese el nombre del responsable: ")
        condiciones_climaticas = input("Ingrese las condiciones climáticas: ")
        
        actividad = {
            "fecha_hora": fecha_hora.strftime("%Y-%m-%d %H:%M"),
            "usuario": usuario_actual,
            "descripcion": descripcion,
            "responsable": responsable,
            "condiciones_climaticas": condiciones_climaticas
        }
        actividades.append(actividad)
        print("Actividad registrada exitosamente.")

    
    def consultar_actividad(self):
        
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        if not fecha_inicio or not fecha_fin:
            raise ErrorNoFechas()
        try:
            fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fecha_fin = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d")
        except ValueError:
            raise ErrorFechaInvalida()
        
        actividades_filtradas = [act for act in actividades if fecha_inicio <= datetime.datetime.strptime(act['fecha_hora'], "%Y-%m-%d %H:%M") <= fecha_fin]
        
        if not actividades_filtradas:
            print("No hay actividades en el rango de fechas seleccionado.")
            return
        
        print("Actividades en el rango seleccionado:")
        for act in actividades_filtradas:
            print(f"Fecha: {act['fecha_hora']}, Responsable: {act['responsable']}, Descripción: {act['descripcion']}, Clima: {act['condiciones_climaticas']}")
    