import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, v):
        return Vector3D(self.x + v.x, self.y + v.y, self.z + v.z)
    def __mul__(self, r):
        return Vector3D(self.x * r, self.y * r, self.z * r)
    def norma(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    def normal(self):
        n = self.norma()
        return Vector3D(self.x / n, self.y / n, self.z / n)
    def productoPunto(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z
    def productoCruz(self, v):
        x = self.y * v.z - self.z * v.y
        y = self.z * v.x - self.x * v.z
        z = self.x * v.y - self.y * v.x
        return Vector3D(x, y, z)
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
suma = v1 + v2
print(suma.x, suma.y, suma.z)
escalar = v1 * 2
print(escalar.x, escalar.y, escalar.z)
print(v1.norma())
normal = v1.normal()
print(normal.x, normal.y, normal.z)
print(v1.productoPunto(v2))
cruz = v1.productoCruz(v2)
print(cruz.x, cruz.y, cruz.z)