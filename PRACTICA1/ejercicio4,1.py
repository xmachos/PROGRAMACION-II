#POO(programacion orientada a objetos)#
class Estadistica:
    def __init__(self, datos):
        self.__datos = datos

    def promedio(self):
        suma = 0
        contador = 0

        for numero in self.__datos:
            suma = suma + numero
            contador = contador + 1

        return suma / contador

    def desviacion(self):
        prom = self.promedio()

        suma = 0
        contador = 0

        for numero in self.__datos:
            diferencia = numero - prom
            suma = suma + diferencia * diferencia
            contador = contador + 1

        resultado = (suma / (contador - 1)) ** 0.5
        return resultado


numeros = []

print("Ingrese 10 números:")

contador = 0
while contador < 10:
    valor = float(input())
    numeros.append(valor)
    contador = contador + 1

estadistica = Estadistica(numeros)

print("El promedio es", estadistica.promedio())
print("La desviación estandar es", estadistica.desviacion())
#VENTAJAS DE USAR POO(PROGRAMACION ORIENTADA A OBJETOS)
#-organisacion de los codigos            
#-Facil de entender
#-se puede usar la clase de otro trabajos
#-Facilidad en los diagramas
        