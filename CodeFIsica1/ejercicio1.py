
class velocidad_tiempo:
    def __init__(self):
        self.vf = ()
        self.t = ()

    def Calculo_Velocidad_final(self, vi, a, t):
        self.vf = vi + a * t
        print("la velociad final es " + str(self.vf))

    def calculo_tiempo(self, vf, vi, a):
        self.t = vf - vi / a
        print("el tiempo es :" + str(self.t))

    tp = int(input("calcular: \n1 velocidad final \n2 timpo \n opcion: "))
    if tp == 1:
        vi = float(input("ingrese la velocidad inicial:"))
        a = float(input("ingrese la aceleracion:"))
        t = float(input("ingrese el timpo:"))
        resultado.Calculo_Velocidad_final(vi, a, t)
    elif tp == 2:
        vf = float(input("ingrese la velocidad final:"))
        vi = float(input("ingrese la velocidad inicial:"))
        a = float(input("ingrese la aceleracion:"))
        resultado.calculo_tiempo(vf, vi, a)


resultado = velocidad_tiempo()
