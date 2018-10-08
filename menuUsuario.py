from usuario import Usuario
import getpass
class MenuUsuario:
    def __init__(self, conexion, cursor):
        self.usuario = Usuario(conexion, cursor)

        while True:
            print("1) Crear Usuario")
            print("2) Login")
            print("0) Salir")
            op = input()

            if op == '1':
                self.capturar()
            elif op == '2':
                self.login()
            elif op == '0':
                break

    def capturar(self):
        usuario = input("Correo: ")
        contra = getpass.getpass("Contraseña: ")
        tipo = input("Tipo: ")
        self.usuario.crear(usuario, contra, tipo)

    def login(self):
        usuario = input("Correo: ")
        contra = getpass.getpass("Contraseña: ")

        if self.usuario.login(usuario, contra):
            print("Bienvenido")
        else:
            print("Usuario/Contraseña incorrectos")
