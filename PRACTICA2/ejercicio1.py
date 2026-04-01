import math
class MiPunto:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distancia(self, *args):
        if len(args) == 1:
            p = args[0]
            dx = self.__x - p.getX()
            dy = self.__y - p.getY()
            return math.sqrt(dx * dx + dy * dy)
        elif len(args) == 2:
            x = args[0]
            y = args[1]
            dx = self.__x - x
            dy = self.__y - y
            return math.sqrt(dx * dx + dy * dy)
p1 = MiPunto()
p2 = MiPunto(10, 30.5)
d = p1.distancia(p2)
print(d)