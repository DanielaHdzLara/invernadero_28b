from registro import Registro
from datetime import datetime, date

class MenuRegistro:
    def __init__(self, conexion, cursor):
        self.registro = Registro(conexion, cursor)

        while True:
            print("1) Agregar Registro")
            print("2) Buscar Registro")
            print("0) Salir")
            op = input()

            if op == "1":
                self.agregar()
            elif op =="2":
                self.buscar()
            elif op == "0":
                break

    def agregar(self):
        id_planta = input("id_planta: ")
        if self.registro.existePlanta(id_planta) == 1:
            print ("Planta inexistente")
        else:
            dia = input("Dia: ")
            mes = input("Mes: ")
            year = input("Año: ")
            fecha = date(int(year), int(mes), int(dia))
            ph = input("PH: ")
            luz = input("Luz: ")
            humedad = input("Humedad: ")
            co2 = input("CO2: ")
            self.registro.agregar(fecha, ph, luz, humedad, co2, id_planta)

    def buscar(self):
        id_planta= input("Id planta: ")
        resultados = self.registro.buscar(id_planta)

        for p in resultados:
            print("ID: {0:2} \nFecha: {1:10} \nPH:........ {2:5} \nLuz:.......{3:5} \nHumedad:... {4:5} \nCO2:....... {5:5}\n".
            format(p[0], str(p[1]), p[2], p[3], p[4], p[5]))
