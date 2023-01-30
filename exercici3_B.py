#te permite saber si hay que hacer la declaracion de la renta

def ingresos ():
    edad = int(input("introduzca su edad: "))
    sueldo = int(input("introduzca su sueldo"))
    if (edad>=18 and sueldo>1200):
        resultado = ("Es necesario que hagas la declaración de hacienda")
    else:
        resultado = ("Aún no puedes hacer la declaración")
    return resultado

print(ingresos())