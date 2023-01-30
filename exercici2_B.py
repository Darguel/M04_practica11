def parImpar ():
    valor = int(input("introduzca un valor"))
    if (valor % 2 == 0):
        resultado = ("El {valor} es par".format(valor=valor))
    else:
        resultado = ("El {valor} es impar".format(valor=valor))
    return resultado

print(parImpar())


