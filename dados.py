# Meu primeiro programa
# Ruan Felipe Bodnar <RuanFelipeBodnar@outlook.com

from random import randint  # Importa a função de gerar números aleatórios

print("Jogo dos dados:")

dado1 = randint(1, 6)  # gera um número entre 1 e 6 aleatóriamente
print("Dado 1: ", dado1)

dado2 = randint(1, 6)  # gera um número entre 1 e 6 aleatóriamente
print("Dado 2: ", dado2)

dado3 = randint(1, 6)  # gera um número entre 1 e 6 aleatóriamente 
print("Dado 3: ", dado3)

dado4 = randint(1, 6)  # gera um número entre 1 e 6 aleatóriamente
print("Dado 4: ", dado4)

Jogador1 = dado1 + dado2
Jogador2 = dado3 + dado4

print('Jogador 1: ', Jogador1)
print('Jogador 2: ', Jogador2)

if Jogador1 > Jogador2:
    print('Jogador 1 venceu!')
else:
    if Jogador2 > Jogador1:
        print('Jogador 2 venceu!')
    else:
        print("Empate!")
        