def generalClave(login,rol):
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    listaPlana = list(caracteres)
    listaCifrada = listaPlana.reverse()
    clave = ""
    login = list(login)
    i = 0
    while i < rol:
        letra = login[i]
        j = listaPlana.index(letra)
        clave = clave + listaCifrada[8]
        i = i + 1
    return clave
rol = 8
