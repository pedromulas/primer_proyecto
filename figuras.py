import math
class figura():
    def __init__(self):
        pass
    def area(self):
        return None
    def perimetro(self):
        return None

class circulo(figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        area = self.radio**2 * math.pi
        return area
    def perimetro(self):
        perimetro = 2*math.pi * self.radio
        return perimetro

c = circulo(4)
print(c.area(), c.perimetro())
