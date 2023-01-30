#pide dos valores y te dira caul es mayor y cual es menor

def mayorValor():
    x = input("introduzca el primer valor: ")
    y = input("introduzca el segundo valor: ")
    if(x>y):
        resultado = ("el numero mas grande es {x} y el mas pequeño es {y}".format(x=x,y=y))
    elif (y>x):
        resultado = ("el numero mas grande es {y} y el mas pequeño es {x}".format(x=x,y=y))
    return resultado
print(mayorValor())