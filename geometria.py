import math
class Circulo:
    raio = None
    centro = None

    def __init__(self, raio, centro):
        self.raio = raio
        self.centro = centro

    def imprime_dados(self):
        print(f'O valor do raio eh {self.raio}')
        print(f'O valor do centro eh {self.centro}')
        print(f'O valor da area do circulo eh {self.area()}')
        print(f'O valor do perimetro do circulo eh {self.perimetro()}')

    def area(self):
        return math.pi*math.pow(self.raio, 2)

    def perimetro(self):
        return math.pi*self.raio*2

    def dentro(self, ponto):
        if distancia(self.centro, ponto) <= self.raio:
            return True
        else:
            return False


def distancia(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


