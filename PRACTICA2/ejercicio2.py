import math
class AlgebraVectorial:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def norma(self, v):
        suma = 0
        i = 0
        while i < len(v):
            suma = suma + v[i] * v[i]
            i = i + 1
        return math.sqrt(suma)

    def suma(self):
        return [self.a[0] + self.b[0], self.a[1] + self.b[1], self.a[2] + self.b[2]]

    def resta(self):
        return [self.a[0] - self.b[0], self.a[1] - self.b[1], self.a[2] - self.b[2]]

    def producto_punto(self):
        return self.a[0]*self.b[0] + self.a[1]*self.b[1] + self.a[2]*self.b[2]

    def producto_cruz(self):
        x = self.a[1]*self.b[2] - self.a[2]*self.b[1]
        y = self.a[2]*self.b[0] - self.a[0]*self.b[2]
        z = self.a[0]*self.b[1] - self.a[1]*self.b[0]
        return [x, y, z]

    def esPerpendicular1(self):
        suma = self.suma()
        resta = self.resta()
        return self.norma(suma) == self.norma(resta)

    def esPerpendicular2(self):
        r1 = self.resta()
        r2 = [self.b[0] - self.a[0], self.b[1] - self.a[1], self.b[2] - self.a[2]]
        return self.norma(r1) == self.norma(r2)

    def esPerpendicular3(self):
        return self.producto_punto() == 0

    def esPerpendicular4(self):
        suma = self.suma()
        izq = self.norma(suma) * self.norma(suma)
        der = self.norma(self.a) * self.norma(self.a) + self.norma(self.b) * self.norma(self.b)
        return izq == der

    def esParalela1(self):
        if self.b[0] != 0:
            r = self.a[0] / self.b[0]
            return self.a[1] == r * self.b[1] and self.a[2] == r * self.b[2]
        return False

    def esParalela2(self):
        cruz = self.producto_cruz()
        return cruz[0] == 0 and cruz[1] == 0 and cruz[2] == 0

    def proyeccion(self):
        punto = self.producto_punto()
        norma_b = self.norma(self.b)
        escalar = punto / (norma_b * norma_b)
        return [escalar * self.b[0], escalar * self.b[1], escalar * self.b[2]]

    def componente(self):
        punto = self.producto_punto()
        norma_b = self.norma(self.b)
        return punto / norma_b


a = [1, 2, 3]
b = [4, 5, 6]

obj = AlgebraVectorial(a, b)

print(obj.esPerpendicular1())
print(obj.esPerpendicular2())
print(obj.esPerpendicular3())
print(obj.esPerpendicular4())
print(obj.esParalela1())
print(obj.esParalela2())
print(obj.proyeccion())
print(obj.componente())