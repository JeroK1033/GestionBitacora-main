import datetime

import pytest
import unittest

from SRC.model.errores_actividad import ErrorDescripcion,ErrorFechaHora,ErrorFechaHoraInvalida, ErrorFechaInvalida, ErrorNoFechas, ErrorSesionNoIniciada, ErrorNoAnexos
from SRC.model.errores_usuario import ErrorNoEmail,ErrorEmailNo,ErrorEmailYa,ErrorContraseñaCorta,ErrorContraseñaIncorrecta,ErrorContraseñaAnteriorIn,ErrorContraseñaNoCoincide
from SRC.model.actividad import Actividad,Archivo
from SRC.model.supervisor import Supervisor, Reporte

class RegistrarActividad(unittest.TestCase):

    def test_registro_actividad_normal(self):
        supervisor = Supervisor("Juan Perez", "juanp225@gmail.com", "JuanPz4875")
        anexo = Archivo("InfoProyecto.pdf", "pdf", "/documentos/InfoProyecto.pdf")
        actividad = Actividad(232245, datetime.datetime.strptime("2025-3-8 15:36", "%Y-%m-%d %H:%M"), "Juan Perez", "Inicio de Nuevo Proyecto", "Nublado y Lluvioso", [anexo], supervisor)
        assert actividad.registrar_actividad()

    def test_registro_actividad_con_fecha_hora(self):
        supervisor = Supervisor("Lucas Correa", "lucasc998@gmail.com", "LucasC2024")
        anexo = Archivo("ProyectoReorganizado.docx", "docx", "/documentos/ProyectoReorganizado.docx")
        actividad = Actividad(498521, datetime.datetime.strptime("2024-11-16 22:45", "%Y-%m-%d %H:%M"), "Lucas Correa", "Revision de Proyecto", "Soleado", [anexo], supervisor)
        assert actividad.registrar_actividad()

    def test_registro_actividad_con_anexo(self):
        supervisor = Supervisor("Maria Hernandez", "maria_hdz87@gmail.com", "MariaH3056")
        anexo = Archivo("EvidenciasMetro.pdf", "pdf", "/documentos/EvidenciasMetro.pdf")
        actividad = Actividad(984216, datetime.datetime.strptime("2025-8-1 8:27", "%Y-%m-%d %H:%M"), "Maria Hernandez", "Evidencias y Avances Metro Bogota", "Neblina", [anexo], supervisor)
        assert actividad.registrar_actividad()

    def test_registro_actividad_limite_dia(self):
        supervisor = Supervisor("Mateo Herrera", "mateoh993@gmail.com", "MateoH7621")
        anexo = Archivo("Especificaciones_Tecnicas.pdf", "pdf", "/documentos/Especificaciones_Tecnicas.pdf")
        actividad = Actividad(284719, datetime.datetime.strptime("2025-11-3 19:40", "%Y-%m-%d %H:%M"), "Mateo Herrera", "Detalles técnicos y normativas del diseño", "Tormenta", [anexo], supervisor)
        assert actividad.registrar_actividad()

    def test_registro_actividad_multiples_anexos(self):
        supervisor = Supervisor("Camila Rodriguez", "camila.rodr@gmail.com", "CamilaR4823")
        anexos = [Archivo("Presentacion_Proyecto.pptx", "pptx", "/documentos/Presentacion_Proyecto.pptx")]
        actividad = Actividad(630582, datetime.datetime.strptime("2024-6-18 14:20", "%Y-%m-%d %H:%M"), "Camila Rodriguez", "Diapositivas con información general del proyecto", "Soleado", anexos, supervisor)
        assert actividad.registrar_actividad()

    def test_registro_actividad_descripcion_larga(self):
        supervisor = Supervisor("Alejandro Fernandez", "alejandrofz23@gmail.com", "AlexF9052")
        anexo = Archivo("Render_Fachada.png", "png", "/documentos/Render_Fachada.png")
        descripcion_larga = "Imagenes digitales del diseño exterior del proyecto"
        actividad = Actividad(157943, datetime.datetime.strptime("2023-12-25 8:55", "%Y-%m-%d %H:%M"), "Alejandro Fernandez", descripcion_larga, "Soleado", [anexo], supervisor)
        assert actividad.registrar_actividad()



    def test_registro_actividad_sin_descripcion(self):
        supervisor = Supervisor("Santiago Rodriguez", "santi_rz99@gmail.com", "SantiR6638")
        anexo = Archivo("Presupuesto_Obra.xlsx", "xlsx", "/documentos/Presupuesto_Obra.xlsx")
        actividad = Actividad(902356, datetime.datetime.strptime("2025-7-7 22:30", "%Y-%m-%d %H:%M"), "Lucas Correa","", "No Aplica", [anexo], supervisor)
        with self.assertRaises(ErrorDescripcion):
            Actividad.registrar_actividad(actividad)

    def test_registro_actividad_fecha_invalida(self):
        supervisor = Supervisor("Valentina Gomez","valentina.gm12@gmail.com","ValenG3721")
        anexo = Archivo("Planos_Estructurales.pdf", "pdf", "/documentos/Planos_Estructurales.pdf")
        actividad = Actividad(418275, "30 de Octubre de 2025", "Valentina Gomez", "La cubierta instalada", "Lluvioso", [anexo],supervisor)
        with self.assertRaises(ErrorFechaHoraInvalida):
            actividad.registrar_actividad()

    def test_registro_actividad_sin_anexos(self):
        supervisor = Supervisor("Camila Rodriguez", "camila.rodr@gmail.com", "CamilaR4823")
        actividad = Actividad(765901, datetime.datetime.strptime("2023-2-14 16:45", "%Y-%m-%d %H:%M"), "Camila Rodriguez", "Las paredes listas para acabados", "Nublado", None, supervisor)
        with self.assertRaises(ErrorNoAnexos):
            actividad.registrar_actividad()

    def test_generar_reporte_rango_valido(self):
        supervisor = Supervisor("Juan Perez", "juanp225@gmail.com", "JuanPz4875")
        reporte = Actividad.generar_reporte(
            (datetime.datetime(2024, 1, 1), datetime.datetime(2024, 12, 31), supervisor, True))
        assert reporte

    def test_generar_reporte_sin_actividades(self):
        supervisor = Supervisor("Maria Hernandez", "maria_hdz87@gmail.com", "MariaH3056")
        reporte = Actividad.generar_reporte(
            (datetime.datetime(2030, 1, 1), datetime.datetime(2030, 12, 31), supervisor, True))
        assert reporte

    def test_generar_reporte_con_anexos(self):
        supervisor = Supervisor("Camila Rodriguez", "camila.rodr@gmail.com", "CamilaR4823")
        reporte = Actividad.generar_reporte(
            (datetime.datetime(2024, 6, 1), datetime.datetime(2024, 6, 10), supervisor, True))
        assert reporte

    def test_generar_reporte_rango_grande(self):
        supervisor = Supervisor("Mateo Herrera", "mateoh993@gmail.com", "MateoH7621")
        reporte = Actividad.generar_reporte(
            (datetime.datetime(2020, 1, 1), datetime.datetime(2025, 12, 31), supervisor, True))
        assert reporte

    def test_generar_reporte_formato_grande(self):
        supervisor = Supervisor("Alejandro Fernandez", "alejandrofz23@gmail.com", "AlexF9052")
        reporte = Actividad.generar_reporte(
            (datetime.datetime(2024, 1, 1), datetime.datetime(2024, 12, 31), supervisor, "A3"))
        assert reporte

    def test_generar_reporte_sin_fechas(self):
        supervisor = Supervisor("Valentina Gomez", "valentina.gm12@gmail.com", "ValenG3721")
        with pytest.raises(ErrorNoFechas):
            Actividad.generar_reporte((None, None, supervisor, True))

    def test_generar_reporte_fechas_invalidas(self):
        supervisor = Supervisor("Camila Rodriguez", "camila.rodr@gmail.com", "CamilaR4823")
        with pytest.raises(ErrorFechaInvalida):
            Actividad.generar_reporte((datetime.datetime(2025, 8, 8), datetime.datetime(2024, 7, 7), supervisor, True))

    def test_generar_reporte_sin_autenticacion(self):
        with pytest.raises(ErrorSesionNoIniciada):
            Actividad.generar_reporte((datetime.datetime(2024, 1, 1), datetime.datetime(2024, 12, 31), None, True))

class ConsultarActividad(unittest.TestCase):

    def test_consulta_rango_valido(self):
        supervisor = Supervisor("Juan Perez", "juanp225@gmail.com", "JuanPz4875")
        actividades = Actividad.consultar_actividad((datetime.datetime(2024, 6, 1), datetime.datetime(2024, 6, 10),supervisor))
        assert actividades

    def test_consulta_fecha_especifica(self):
        supervisor = Supervisor("Juan Perez", "juanp225@gmail.com", "JuanPz4875")
        actividades = Actividad.consultar_actividad((datetime.datetime(2024, 6, 1), datetime.datetime(2024, 6, 1), supervisor))
        assert actividades

    def test_consulta_con_filtros(self):
        supervisor = Supervisor("Juan Perez", "juanp225@gmail.com", "JuanPz4875")
        condiciones_climaticas: str = "Neblina"
        actividades = Actividad.consultar_actividad((datetime.datetime(2024, 6, 1), datetime.datetime(2024, 6, 10), supervisor, condiciones_climaticas))
        assert actividades

    def test_consulta_rango_grande(self):
        supervisor = Supervisor("Juan Perez", "juanp225@gmail.com", "JuanPz4875")
        actividades = Actividad.consultar_actividad((datetime.datetime(2023, 1, 1), datetime.datetime(2025, 12, 31), supervisor))
        assert actividades

    def test_consulta_multiples_filtros(self):
        supervisor = Supervisor("Camila Rodriguez", "camila.rodr@gmail.com", "CamilaR4823")
        condiciones_climaticas: str = "soleado"
        descripcion: str = "Proyecto"
        actividades = Actividad.consultar_actividad(
            (datetime.datetime(2024, 6, 1), datetime.datetime(2024, 6, 10), supervisor, condiciones_climaticas, descripcion))
        assert actividades

    def test_consulta_fecha_futura(self):
        supervisor = Supervisor("Juan Perez", "juanp225@gmail.com", "JuanPz4875")
        actividades = Actividad.consultar_actividad((datetime.datetime(2030, 1, 1), datetime.datetime(2030, 12, 31), supervisor))
        assert actividades

    def test_consulta_fecha_inicio_mayor(self):
        supervisor = Supervisor("Juan Perez", "juanp225@gmail.com", "JuanPz4875")
        with self.assertRaises(ErrorFechaInvalida):
            Actividad.consultar_actividad((datetime.datetime(2025, 8, 8), datetime.datetime(2024, 7, 7), supervisor))

    def test_consulta_sin_fechas(self):
        supervisor = Supervisor("Juan Perez", "juanp225@gmail.com", "JuanPz4875")
        with self.assertRaises(ErrorNoFechas):
            Actividad.consultar_actividad((None, None, supervisor))

    def test_consulta_sin_autenticacion(self):
        with self.assertRaises(ErrorSesionNoIniciada):
            Actividad.consultar_actividad((datetime.datetime(2023, 1, 1), datetime.datetime(2025, 12, 31), None))
    pass

class GenerarReporte(unittest.TestCase):
    def test_generar_reporte_rango_valido(self):
        supervisor = Supervisor("Juan Perez", "juanp225@gmail.com", "JuanPz4875")
        reporte = Reporte.generar_reporte(
            (datetime.datetime(2024, 1, 1), datetime.datetime(2024, 12, 31), supervisor, True))
        assert reporte

    def test_generar_reporte_sin_actividades(self):
        supervisor = Supervisor("Maria Hernandez", "maria_hdz87@gmail.com", "MariaH3056")
        reporte = Reporte.generar_reporte(
            (datetime.datetime(2030, 1, 1), datetime.datetime(2030, 12, 31), supervisor, True))
        assert reporte

    def test_generar_reporte_con_anexos(self):
        supervisor = Supervisor("Camila Rodriguez", "camila.rodr@gmail.com", "CamilaR4823")
        reporte = Reporte.generar_reporte(
            (datetime.datetime(2024, 6, 1), datetime.datetime(2024, 6, 10), supervisor, True))
        assert reporte

    def test_generar_reporte_rango_grande(self):
        supervisor = Supervisor("Mateo Herrera", "mateoh993@gmail.com", "MateoH7621")
        reporte = Reporte.generar_reporte(
            (datetime.datetime(2020, 1, 1), datetime.datetime(2025, 12, 31), supervisor, True))
        assert reporte

    def test_generar_reporte_formato_grande(self):
        supervisor = Supervisor("Alejandro Fernandez", "alejandrofz23@gmail.com", "AlexF9052")
        reporte = Reporte.generar_reporte(
            (datetime.datetime(2024, 1, 1), datetime.datetime(2024, 12, 31), supervisor, "A3"))
        assert reporte

    def test_generar_reporte_sin_fechas(self):
        supervisor = Supervisor("Valentina Gomez", "valentina.gm12@gmail.com", "ValenG3721")
        with self.assertRaises(ErrorNoFechas):
            Reporte.generar_reporte((None, None, supervisor, True))

    def test_generar_reporte_fechas_invalidas(self):
        supervisor = Supervisor("Camila Rodriguez", "camila.rodr@gmail.com", "CamilaR4823")
        with self.assertRaises(ErrorFechaInvalida):
            Reporte.generar_reporte((datetime.datetime(2025, 8, 8), datetime.datetime(2024, 7, 7), supervisor, True))

    def test_generar_reporte_sin_autenticacion(self):
        with self.assertRaises(ErrorSesionNoIniciada):
            Reporte.generar_reporte((datetime.datetime(2024, 1, 1), datetime.datetime(2024, 12, 31), None, True))


class CrearCuenta(unittest.TestCase):
    def test_registro_exitoso(self):
        usuario = Supervisor("Juan Perez", "juan.perez@example.com", "JuanP@123")
        assert usuario is False

    def test_registro_con_email_valido(self):
        usuario = Supervisor("Maria Lopez", "maria.lopez@example.com", "Maria2024#")
        assert usuario is False

    def test_registro_con_nombre_apellido_validos(self):
        usuario = Supervisor("Carlos Rivera", "carlos.r@example.com", "Carlos2024#")
        assert usuario is False

    def test_registro_contraseña_larga(self):
        usuario = Supervisor("Luis Gómez", "luis.gomez@example.com", "32CaracteresLargos1234#@")
        assert usuario is False

    def test_registro_caracteres_especiales_nombre(self):
        usuario = Supervisor("Ana-María López", "ana.lopez@example.com", "AnaFuerte2024!")
        assert usuario is False

    def test_registro_sin_email(self):
        with self.assertRaises(ErrorNoEmail):
            Supervisor("Carlos Rivera", None, "Carlos2024")

    def test_registro_contraseña_corta(self):
        with self.assertRaises(ErrorContraseñaCorta):
            Supervisor("Luis Gómez", "luis.gomez@example.com", "123")

    def test_registro_email_ya_registrado(self):
        with self.assertRaises(ErrorEmailYa):
            Supervisor("Juan Perez", "juan.perez@example.com", "JuanP@123")

class IniciarSesion(unittest.TestCase):
    def test_inicio_sesion_exitoso(self):
        usuario = Supervisor("Juan Perez", "juan.perez@gmail.com", "JuanP@123")
        assert usuario.iniciar_sesion()

    def test_inicio_sesion_recordar_activado(self):
        usuario = Supervisor("Maria Lopez", "MARIA.LOPEZ@EXAMPLE.COM", "Maria2024#")
        assert usuario.iniciar_sesion()

    def test_inicio_sesion_varios_intentos(self):
        usuario = Supervisor("Carlos Rivera", "carlos.r@gmail.com", "Carlos2024#")
        assert usuario.iniciar_sesion()

    def test_inicio_sesion_contraseña_larga(self):
        usuario = Supervisor("Luis Gómez", "luis.gomez@gmail.com", "32CaracteresLargos1234#@")
        assert usuario.iniciar_sesion()

    def test_inicio_sesion_solo_letras_minusculas(self):
        usuario = Supervisor("Maria Lopez", "maria.lopez@gmail.com", "mariaclave")
        assert usuario.iniciar_sesion()

    def test_inicio_sesion_solo_numeros(self):
        usuario = Supervisor("Carlos Rivera", "carlos.r@gmail.com", "12345678")
        assert usuario.iniciar_sesion()

    def test_inicio_sesion_contraseña_incorrecta(self):
        usuario = Supervisor("Juan Perez", "juan.perez@gmail.com", "Incorrecta123")
        with self.assertRaises(ErrorContraseñaIncorrecta):
            usuario.iniciar_sesion()

    def test_inicio_sesion_email_no_registrado(self):
        usuario = Supervisor("Usuario Nuevo", "usuario.nuevo@gmail.com", "NuevaClave@456")
        with self.assertRaises(ErrorEmailNo):
            usuario.iniciar_sesion()

    def test_inicio_sesion_formato_email_invalido(self):
        usuario = Supervisor("Usuario Incorrecto", "incorrecto.com", "Prueba2024#")
        with self.assertRaises(ErrorEmailNo):
            usuario.iniciar_sesion()


class CambiarContraseña(unittest.TestCase):
    def test_cambio_contraseña_exitoso(self):
        usuario = Supervisor("Juan Perez", "juan.perez@gmail.com", "JuanP@123")
        assert usuario.cambiar_contraseña("JuanP@456")

    def test_cambio_contraseña_fuerte(self):
        usuario = Supervisor("Maria Lopez", "maria.lopez@gmail.com", "Maria2024#")
        assert usuario.cambiar_contraseña("MariaFuerte2024!")

    def test_cambio_contraseña_y_login(self):
        usuario = Supervisor("Juan Perez", "juan.perez@gmail.com", "JuanP@456")
        assert usuario.iniciar_sesion()

    def test_cambio_contraseña_larga(self):
        usuario = Supervisor("Luis Gómez", "luis.gomez@gmail.com", "Luis2023")
        assert usuario.cambiar_contraseña("32CaracteresLargos1234#@")

    def test_cambio_contraseña_caracteres_especiales(self):
        usuario = Supervisor("Maria Lopez", "maria.lopez@gmail.com", "Maria2024#")
        assert usuario.cambiar_contraseña("@#$%^&*()_+")

    def test_cambio_contraseña_caracteres_especiales_y_numeros(self):
        usuario = Supervisor("Carlos Rivera", "carlos.r@gmail.com", "Carlos2024#")
        assert usuario.cambiar_contraseña("C@rlos1234!")

    def test_cambio_contraseña_contraseña_anterior_incorrecta(self):
        usuario = Supervisor("Juan Perez", "juan.perez@gmail.com", "JuanP@123")
        with self.assertRaises(ErrorContraseñaAnteriorIn):
            usuario.cambiar_contraseña("Incorrecta123")

    def test_cambio_contraseña_no_coincide(self):
        usuario = Supervisor("Luis Gómez", "luis.gomez@gmail.com", "Luis2023")
        with self.assertRaises(ErrorContraseñaNoCoincide):
            usuario.cambiar_contraseña("LuisNuevo2024", "LuisDiferente2024")

    def test_cambio_contraseña_sin_autenticacion(self):
        with self.assertRaises(ErrorEmailNo):
            Supervisor(None, None, None).cambiar_contraseña("NuevaClave@2025")
