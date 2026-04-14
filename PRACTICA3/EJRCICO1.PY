import random

class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
        self.vidasActuales = numeroDeVidas
    def reiniciaPartida(self):
        self.vidasActuales = self.numeroDeVidas
    def actualizaRecord(self):
        if self.vidasActuales > self.record:
            self.record = self.vidasActuales
            print("Nuevo record:", self.record)
    def quitaVida(self):
        self.vidasActuales = self.vidasActuales - 1
        if self.vidasActuales > 0:
            return True
        else:
            return False
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10:
            return True
        else:
            return False
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("Adivina un número entre 0 y 10")

        while True:
            numeroIngresado = int(input("Ingresa un número: "))

            if self.validaNumero(numeroIngresado) == False:
                print("Número inválido, intenta nuevamente")
            else:
                if numeroIngresado == self.numeroAAdivinar:
                    print("Acertaste!!")
                    self.actualizaRecord()
                    break
                else:
                    resultado = self.quitaVida()

                    if resultado == True:
                        if numeroIngresado < self.numeroAAdivinar:
                            print("El número a adivinar es mayor")
                        else:
                            print("El número a adivinar es menor")
                    else:
                        print("Te quedaste sin vidas")
                        print("El número era:", self.numeroAAdivinar)
                        break
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10:
            if numero % 2 == 0:
                return True
            else:
                print("Error: el número es impar, debe ser par")
                return False
        else:
            return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10:
            if numero % 2 != 0:
                return True
            else:
                print("Error: el número es par, debe ser impar")
                return False
        else:
            return False


class Aplicacion:
    def main(self):
        juegoNormal = JuegoAdivinaNumero(3)
        juegoPar = JuegoAdivinaPar(3)
        juegoImpar = JuegoAdivinaImpar(3)

        print("----- JUEGO NORMAL -----")
        juegoNormal.juega()

        print("\n----- JUEGO PARES -----")
        juegoPar.juega()

        print("\n----- JUEGO IMPARES -----")
        juegoImpar.juega()


if __name__ == "__main__":
    app = Aplicacion()
    app.main()