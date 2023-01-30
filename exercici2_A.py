"""
En aquest arxiu s’hi crearà una funció on demanarà que insereixin un nom dels 5 que es
proposin. Depenent del nom que indiqui s’hi mostrarà, per consola, un missatge diferent.
Si es passa un nom no adeqüat s’ha d’indicar que el nom no està a la llista.
"""
def nombre():
    nombre = input("Elige uno de los siguientes nombres: Luis, David, Alex, Ivan, Itamar: ")
    if (nombre == "Luis" or nombre == "David" or nombre == "Alex" or nombre == "Ivan" or nombre == "Itamar" ):
        solucion = ("{nombre} esta haciendo la practica de python".format(nombre=nombre))
    else:
        solucion = "El nombre escogido no esta en la lista."
    return solucion

print (nombre())
