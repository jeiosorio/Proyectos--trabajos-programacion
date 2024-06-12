def Calculo_Velocidad_final(vi, a, t):
    vf = vi + a * t
    print("la velociad final es " + str(vf))


def calculo_tiempo(vf, vi, a):
    t = vf - vi / a
    print("el tiempo es :" + str(t))


tp = int(input("calcular: \n1 velocidad final \n2 timpo \n opcion: "))
resul = tp
while resul:
    if resul == 1:
        vi = float(input("ingrese la velocidad inicial:"))
        a = float(input("ingrese la aceleracion:"))
        t = float(input("ingrese el timpo:"))
        Calculo_Velocidad_final(vi, a, t)
    elif resul == 2:
        vf = float(input("ingrese la velocidad final:"))
        vi = float(input("ingrese la velocidad inicial:"))
        a = float(input("ingrese la aceleracion:"))
        calculo_tiempo(vf, vi, a)

    elif resul != 1 and 2:
        print("numero invalido velve a correr el programa : \n1 para calcular velocidad final \n2 para calcular tiempo")
        break




