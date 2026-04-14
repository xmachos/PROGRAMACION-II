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

    # b) uso de validaNumero en juega
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

            if self.validaNumero(numeroIngresado) == False:
                print("Número fuera de rango")
                continue

            if numeroIngresado == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
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
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)

        print("----- JUEGO NORMAL -----")
        juego1.juega()
        print("\n----- JUEGO PARES -----")
        juego2.juega()
        print("\n----- JUEGO IMPARES -----")
        juego3.juega()
if __name__ == "__main__":
    app = Aplicacion()
    app.main()