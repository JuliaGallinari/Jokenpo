import random

# Função que valida número inteiro dentro de um intervalo definido
def valida_int(pergunta, min, max):
    while True:
        try:
            x = int(input(pergunta))
            if min <= x <= max:
                return x
            print('Opção inválida, digite um número entre {} e {}.'.format(min, max))
        except ValueError:
            print('Opção inválida, digite um número inteiro entre {} e {}.'.format(min, max))

# Função para validar quem é o vencedor da jogada e armazenar quantidade de vitorias e empates
def jogos(jogador1, jogador2):
    global empate, vitoria1, vitoria2
    if jogador1 == jogador2:
        empate += 1
        print('Jogador 1: {}\n Jogador 2: {}'.format(jogador1, jogador2))
        print('Houve um empate!')
    elif jogador1 == 1 and jogador2 == 3 or jogador1 == 2 and jogador2 == 1 or jogador1 == 3 and jogador2 == 2:
        print('Jogador 1: {}\nJogador 2: {}'.format(jogador1, jogador2))
        print('O jogador 1 venceu esta!')
        vitoria1 += 1
    else:
        print('Jogador 1: {}\nJogador 2: {}'.format(jogador1, jogador2))
        print('O jogador 2 venceu esta!')
        vitoria2 += 1
    resultados = [vitoria1, vitoria2, empate]
    return resultados

# Variáveis a serem usadas
jogadas = []
vitoria1 = 0
vitoria2 = 0
empate = 0

# Menu de opções
print('BEM VINDO AO JOGO DE JOKENPO!')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('0 - Sair')

# Laço de repetição para seleção
while True:
    jogada1 = valida_int('\nDigite sua jogada: ', 0, 3)
    if jogada1 == 0:
        break
    jogada2 = random.randint(1, 3)
    jogadas.append([jogada1, jogada2])
    total = jogos(jogada1, jogada2)

# Imprime o resultado final do jogo
print('O número de vitórias do jogador 1 foi: {}.'.format(total[0]))
print('O número de vitórias do jogador 2 foi: {}.'.format(total[1]))
print('O número de empates entre ambos foi: {}.'.format(total[2]))
