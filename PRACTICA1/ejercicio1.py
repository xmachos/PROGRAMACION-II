import time
class Cronometro:
    def __init__(self):
        self.__inicia = int(time.time() * 1000)
        self.__finaliza = 0

    def get_inicia(self):
        return self.__inicia

    def get_finaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = int(time.time() * 1000)

    def detener(self):
        self.__finaliza = int(time.time() * 1000)

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia

def OrdenacionSeleccion(lista):

    n = len(lista)

    i = 0
    while i < n - 1:

        indice_minimo = i

        j = i + 1
        while j < n:

            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

            j = j + 1

        aux = lista[i]
        lista[i] = lista[indice_minimo]
        lista[indice_minimo] = aux

        i = i + 1

lista_numeros = []

contador = 100000
while contador > 0:
    lista_numeros.append(contador)
    contador = contador - 1
cron = Cronometro()
cron.inicia()
OrdenacionSeleccion(lista_numeros)
cron.detener()
print("Tiempo transcurrido en milisegundos:", cron.lapsoDeTiempo())