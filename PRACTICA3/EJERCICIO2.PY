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
        return self.vidasActuales > 0


class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, numero):
        return 0 <= numero <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("Adivina un número entre 0 y 10")

        while True:
            entrada = input("Ingresa un número: ")

            if not entrada.isdigit():
                print("Error: debes ingresar un número válido")
                continue

            numeroIngresado = int(entrada)

            if not self.validaNumero(numeroIngresado):
                print("Número fuera de rango")
                continue

            if numeroIngresado == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break

            if self.quitaVida():
                if numeroIngresado < self.numeroAAdivinar:
                    print("El número a adivinar es MAYOR")
                else:
                    print("El número a adivinar es MENOR")
            else:
                print("Te quedaste sin vidas")
                print("El número era:", self.numeroAAdivinar)
                break
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 0:
            return True
        print("Error: el número debe ser PAR")
        return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10 and numero % 2 != 0:
            return True
        print("Error: el número debe ser IMPAR")
        return False
class Aplicacion:
    def main(self):
        print("----- JUEGO NORMAL -----")
        JuegoAdivinaNumero(3).juega()

        print("\n----- JUEGO PARES -----")
        JuegoAdivinaPar(3).juega()

        print("\n----- JUEGO IMPARES -----")
        JuegoAdivinaImpar(3).juega()
if __name__ == "__main__":
    Aplicacion().main()