Criar um programa que usa o método de Monte-Carlo para estimar o
valor de π . Isso é possível criando um círculo inscrito em um quadrado, sorteando pontos
aleatórios dentro deste quadrado e calculando a proporção dos pontos que caíram dentro do
círculo em relação a área do quadrado.
Para calcular de forma fácil, sabemos que um círculo de raio = 1 tem área = π e o quadrado
de lado = 2 tem área = 4, portanto sabemos, que um ponto sorteado aleatoriamente, tem
probabilidade π /4 de cair dentro do círculo.
Portanto, sabendo quantos pontos sorteados estão dentro do círculo, conseguimos estimar o
valor π /4, logo conseguimos estimar o valor de π .
Tarefa:
Criar um módulo chamado geometria.py , que deve conter uma classe Circulo , que recebe o
raio e centro no construtor e possui a definição de acordo com o diagrama abaixo, além de uma
função que calcula a distância entre dois pontos dados (tuplas).
Além disso, criar um programa monte_carlo.py , que pergunta ao usuário quantos pontos ele quer
usar para rodar a estimativa e utiliza o módulo e a classe acima para realizar a estimativa de π.
