import math
class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        parte1 = self.__b * self.__b
        parte2 = 4 * self.__a * self.__c
        discriminante = parte1 - parte2
        return discriminante

    def getRaiz1(self):
        discriminante = self.getDiscriminante()

        if discriminante >= 0:
            raiz = math.sqrt(discriminante)
            numerador = -self.__b + raiz
            denominador = 2 * self.__a
            resultado = numerador / denominador
            return resultado
        else:
            return 0

    def getRaiz2(self):
        discriminante = self.getDiscriminante()

        if discriminante >= 0:
            raiz = math.sqrt(discriminante)
            numerador = -self.__b - raiz
            denominador = 2 * self.__a
            resultado = numerador / denominador
            return resultado
        else:
            return 0


# Test del programa
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
ecuacion = EcuacionCuadratica(a, b, c)
discriminante = ecuacion.getDiscriminante()
if discriminante > 0:
    r1 = ecuacion.getRaiz1()
    r2 = ecuacion.getRaiz2()
    print("La ecuacion tiene dos raíces:", r1, "y", r2)
elif discriminante == 0:
    r = ecuacion.getRaiz1()
    print("La ecuaci0n tiene una raiz:", r)
else:
    print("La ecuacion no tiene raices reales")
