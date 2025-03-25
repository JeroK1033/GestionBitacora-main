import sys
import json
from datetime import datetime
from SRC.model.supervisor import Supervisor



usuarios = {}
actividades = []
usuario_actual = None

def guardar_usuarios():
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)

# Función para cargar usuarios de un archivo JSON
def cargar_usuarios():
    global usuarios
    try:
        with open("usuarios.json", "r") as f:
            usuarios = json.load(f)
    except FileNotFoundError:
        usuarios = {}

cargar_usuarios()

class Bitacora:
    
    def menu(self):
        global usuario_actual
        while True:
            if usuario_actual:
                print("\nBienvenido, " + usuarios[usuario_actual]["nombre"])
                print("1. Registrar actividad")
                print("2. Consultar actividades")
                print("3. Generar reporte PDF")
                print("4. Cerrar sesión")
            else:
                print("\nBitacora de Construccion")
                print("1. Registarse")
                print("2. Iniciar sesión")
                print("3. Cambiar contraseña")
                print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if usuario_actual:
                if opcion == "1":
                    self.registrar_actividad()
                elif opcion == "2":
                    self.consultar_actividades()
                elif opcion == "3":
                    self.generar_reporte()
                elif opcion == "4":
                    usuario_actual = None
                    print("Cierre de sesión exitoso.")
                else:
                    print("Opción no válida. Intente de nuevo.")
            else:
                if opcion == "1":
                    Supervisor.registrarse()
                elif opcion == "2":
                    Supervisor.iniciar_sesion()
                elif opcion == "3":
                    Supervisor.cambiar_contraseña()
                elif opcion == "4":
                    print("Saliendo del sistema...")
                    sys.exit()
                else:
                    print("Opción no válida. Intente de nuevo.")
                
if __name__ == "__main__":
    app = Bitacora()
    app.menu()