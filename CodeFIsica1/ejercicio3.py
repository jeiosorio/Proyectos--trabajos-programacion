import math

def Calculo_area_circulo(r):
    area = math.pi * pow(r, 2)
    print("el area del circulo es " + str(area))


def logitud_circunferencia(r):
    long = 2 * math.pi * r
    print("la longitud es :" + str(long))


tp = int(input("calcular: \n1 Calculo_area_circulo \n2 logitud_circunferencia \n opcion: "))
resul = tp
while resul:
    if resul == 1:
        rad = float(input("ingrese el area a calcular:"))

        Calculo_area_circulo(rad)
    elif resul == 2:
        rad = float(input("ingrese ingrese la logitud de la circunferencia a calcular:"))
        logitud_circunferencia(rad)

    elif resul != 1 and 2:
        print("numero invalido velve a correr el programa : \n1 para calcular velocidad final \n2 para calcular tiempo")
        break

