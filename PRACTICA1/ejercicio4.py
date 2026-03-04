#Modular – Estructurada#
def promedio(datos):
    suma = 0
    contador = 0

    for numero in datos:
        suma = suma + numero
        contador = contador + 1

    return suma / contador


def desviacion(datos):
    prom = promedio(datos)

    suma = 0
    contador = 0

    for numero in datos:
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

print("El promedio es", promedio(numeros))
print("La desviación estandar es", desviacion(numeros))