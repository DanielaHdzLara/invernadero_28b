from invernadero import Invernadero
class MenuInvernadero:
    def __init__(self, conexion, cursor):
        self.inv = Invernadero(conexion, cursor)
        while True:
            print("1) Agregar Invernadero")
            print("2) Mostrar Invernadero")
            print("0) Salir")
            op = input()

            if op == "1":
                self.agregar()
            elif op == "2":
                self.mostrar()
            elif op == "0":
                break

    def agregar(self):
        nombre = input("Nombre Invernadero: ")
        ubicacion = input("Ubicación Invernadero: ")
        id_dueno = input("id_dueno: ")
        self.inv.crear(nombre, ubicacion, id_dueno)

    def mostrar(self):
        resultados = []
        for r in resultados:
            print("{0:3} {1:20} {2:20}".format(r[0], r[1], r[2]))
