"""
En aquest arxiu s’hi crearà una funció on demanarà a l’usuari que inserti 2 números i el programa li dirà
quin és el més gran i quin el més petit. Si son iguals sortirà que son iguals.
"""
def mayor():
    num1 = input("Primer numero: ")
    num2 = input("segundo numero: ")
    if (num1>num2):
        solucion = ("El numero mas grande es {num1} y el mas pequeño es {num2}.".format(num1=num1,num2=num2));
    elif (num2>num1):
        solucion = ("El numero mas grande es {num2} y el mas pequeño es {num1}.".format(num1=num1,num2=num2));
    else:
        solucion = ("son iguales");
    return solucion

print (mayor())