import geometria
import random

num = int(input("Quantos pontos quer usar para o teste: "))

centro = (0, 0)

circulo = geometria.Circulo(1, centro)

circulo.imprime_dados()

contDentro = 0

for pontos in range(num):
    p1 = random.uniform(0, 1)
    p2 = random.uniform(0, 1)
    ponto= (p1, p2)
    if circulo.dentro(ponto) is True:
        contDentro += 1

print(4*contDentro/num)
