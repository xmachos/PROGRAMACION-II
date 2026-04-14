import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        self.numeroDeVidas = 3 
    def actualizaRecord(self):
        self.record += 1
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        while True:
            print("\nAdivina el número (0 al 10): ")
            try:
                numero = int(input())
            except:
                print("Ingresa un número válido")
                continue
            if numero == self.numeroAAdivinar:
                print("¡Acertaste!! ")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if numero < self.numeroAAdivinar:
                        print("El número es MAYOR")
                    else:
                        print("El número es MENOR")
                    print("Intenta de nuevo. Vidas restantes:", self.numeroDeVidas)
                else:
                    print("Perdiste  No te quedan vidas")
                    break
class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()
if __name__ == "__main__":
    Aplicacion.main()