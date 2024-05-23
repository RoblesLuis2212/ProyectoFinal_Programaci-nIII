import os
import os.path as path
import time

#Funcion que creara los archivos en caso de que no existan
def CrearArchivos():
    ArchivoGerente = open("Gerente.txt","w")
    ArchivoEmpleado = open("Empleados.txt","w")
    ArchivoContraseña = open("Contraseñas.txt","w")
    ArchivoCliente = open("Clientes.txt","w")
    ArchivoPedidos = open("Direccion.txt","w")
    ArchivoID = open("IdClientes.txt","w")


def LimpiarConsola():
    os.system('cls')


#Funcion Registrarse
def Registro():
    print("------Registro-----")
    
    Nombre = input("Ingrese su nombre: ") 
    Constraseña = input("Ingrese su contraseña: ")
    
    LeerGerente = open("Clientes.txt","a")
    LeerContraseñas = open("Contraseñas.txt","a")
    
    LeerGerente.write(Nombre + '\n')
    LeerContraseñas.write(Constraseña + '\n')
    
    LeerGerente.close()
    LeerContraseñas.close()
    print("Usuario generado correctamente,Gracias por elegirnos")
    time.sleep(3)
    LimpiarConsola()
    MenuClientes()

#Esta funcion permitira al sistema poder identificar que tipo de usuario esta accediendo
def LoginClientes():
    print("-----INICIAR SESION----")
    Usuario = input("Ingrese su nombre: ")
    Contraseña = input("Ingrese su contraseña: ")

    AbrirClientes = open("Clientes.txt","r")
    AbrirContraseñas = open("Contraseñas.txt","r")
    
    ListaClientes = AbrirClientes.readlines()
    ListaContraseña = AbrirContraseñas.readlines()

    if Usuario + '\n' in ListaClientes:
        indice = ListaClientes.index(Usuario + '\n')
        if ListaContraseña[indice] == Contraseña + '\n':
            print("Cliente encontrado en la lista")
            LimpiarConsola()
            MenuComidas()
        else:
            print("Contraseña incorrecta")
    else:
        print("Cliente inexistente")

def Instalador():
    if path.exists("Gerente.txt"):
        print("Archivos encontrados accediendo al sistema...")
        time.sleep(2)
        LimpiarConsola()
        MenuInicio()
    else:
        print("Archivo inexistentes...")
        print("Creando Archivos...")
        time.sleep(3)
        CrearArchivos()
        MenuClientes()
        print("Archivos creados exitosamente")

#Menu para clientes
def MenuClientes():
    print("------SISTEMA DE GASTRONOMIA-----")
    print("1.Registrarse")
    print("2.Iniciar Sesion")
    print("3.Mostrar Menu")
    print("4.Realizar Pedido")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        LimpiarConsola()
        Registro()
    elif opcion == 2:
        LimpiarConsola()
        LoginClientes()


def MenuInicio():
    print("----SISTEMA GASTRONOMICO-----")
    print("1.Iniciar Sesion")
    print("2.Registrarse")
    print("3.Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        LimpiarConsola()
        LoginClientes()
    elif opcion == 2:
        LimpiarConsola()
        Registro()
    elif opcion == 3:
        LimpiarConsola()
        print("Hasta luego vuelva pronto")
        exit()


def MenuComidas():
    print("--------Menu De Comidas------")
    print("1.Fideo Tallerin con salsa")
    print("2.Hamburguesa Especial")
    print("3.Canelones de verdura")
    print("Milanesa Napolitana con pure")
    opcion = input("Seleccione una opcion: ")



Instalador()