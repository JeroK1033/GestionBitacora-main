from abc import ABC
import datetime
from errores_usuario import ErrorEmailNo, ErrorEmailYa, ErrorContraseñaCorta, ErrorCamposIncompletos
from main import guardar_usuarios
from fpdf import FPDF

global usuario_actual, actividades, usuarios

class Supervisor():
    
    def __init__(self, nombre: str, correo: str, contraseña: str):
        self.contraseña = contraseña
        self.correo = correo
        self.nombre = nombre
    
    @staticmethod
    def cambiar_contraseña_supervisor()->str:
        correo = input("Ingrese su correo: ")
        if correo in usuarios:
            contrasena_actual = input("Ingrese su contraseña actual: ")
            if usuarios[correo]["contraseña"] == contrasena_actual:
                nueva_contraseña = input("Ingrese su nueva contraseña: ")
                if len(nueva_contraseña) < 6:
                    raise ErrorContraseñaCorta("La nueva contraseña debe tener al menos 6 caracteres.")
                usuarios[correo]["contraseña"] = nueva_contraseña
                guardar_usuarios()
                print("Contraseña cambiada exitosamente.")
            else:
                print("Contraseña actual incorrecta.")
        else:
            print("Correo no encontrado.")
            
    
    @staticmethod
    def iniciar_sesion():
        global usuario_actual
        correo = input("Ingrese su correo: ")
        contraseña = input("Ingrese su contraseña: ")
        if correo in usuarios and usuarios[correo]["contraseña"] == contraseña:
            usuario_actual = correo
            print("Inicio de sesión exitoso.")
        else:
            print("Correo o contraseña incorrectos.")

    @staticmethod
    def registrarse(nombre: str, correo: str, contraseña: str):
        try:
            nombre = input("Ingrese su nombre: ")
            correo = input("Ingrese su correo: ")
            if "@" not in correo:
                raise ErrorEmailNo
            if correo in usuarios:
                raise ErrorEmailYa
            contraseña = input("Ingrese su contraseña: ")
            if len(contraseña) < 8:
                raise ErrorContraseñaCorta
            usuarios[correo] = Supervisor(nombre, correo, contraseña)
            print("Registro exitoso.")
        except ErrorCamposIncompletos:
            print("Por favor, llene todos los campos.")
            
    
class Reporte:
    def __init__(self, idreporte: int, rangofecha: datetime, contenido: str):
        self.contenido = contenido
        self.rangoFecha = rangofecha
        self.idReporte = idreporte
    
    def generar_reporte(self):
        
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        try:
            fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fecha_fin = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha incorrecto.")
            return
        
        actividades_filtradas = [act for act in actividades if fecha_inicio <= datetime.datetime.strptime(act['fecha_hora'], "%Y-%m-%d %H:%M") <= fecha_fin]
        
        if not actividades_filtradas:
            print("No hay actividades en el rango de fechas seleccionado.")
            return
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, "Reporte de Bitácora", ln=True, align="C")
        pdf.ln(10)
        for actividad in actividades_filtradas:
            pdf.cell(200, 10, f"Fecha: {actividad['fecha_hora']}", ln=True)
            pdf.cell(200, 10, f"Responsable: {actividad['responsable']}", ln=True)
            pdf.cell(200, 10, f"Descripción: {actividad['descripcion']}", ln=True)
            pdf.cell(200, 10, f"Condiciones Climáticas: {actividad['condicion']}", ln=True)
            pdf.ln(10)
        pdf.output("reporte_bitacora.pdf")
        print("Reporte generado exitosamente: reporte_bitacora.pdf")