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

    if Usuario in ListaClientes and Contraseña in ListaContraseña:
        print("Cliente encontrado en la lista")
    else:
        print("Cliente inexistente") #Mostramos error si el usuario o contraseña no son encontrados

def Instalador():
    if path.exists("Gerente.txt"):
        print("Archivos encontrados accediendo al sistema...")
        MenuClientes()
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
        Registro()
    elif opcion == 2:
        LoginClientes()





Instalador()