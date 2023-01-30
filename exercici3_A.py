import random

def aleatorio():
    miNum = random.randrange(0,101)
    tuNum = int(input("Elige un numero entre el 0 y el 100: "))
    if (miNum == tuNum):
        solucion = ("Molt bé! Has endevinat el número!")
    elif (miNum > tuNum):
        print ("El número és més gran")
    elif (miNum < tuNum):
        print ("El número és més petit")

print(aleatorio())