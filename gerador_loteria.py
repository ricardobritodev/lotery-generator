import random
import time


def gerador_megasena():
    print("=====" * 16)
    print("===" * 8, "  GERADOR DE APOSTA MEGASENA  ", "===" * 8)
    print("=====" * 16)

    numero_jogos = int(input(">> Digite o número de jogos: "))
    jogo = 0
    resultado = []

    for linha in range(int(numero_jogos)):
        jogo += 1
        numeros = random.sample(range(1, 61), 6)

        for coluna in range(1):
            numeros = random.sample(range(1, 61), 6)
            print(f'>> Jogo {jogo}: ')
            print(numeros, end='')

        print()
        print("---" * 20)
        time.sleep(1)
        resultado.append(numeros)

    print("===" * 8, "Boa sorte!", "===" * 8)
    return resultado

def gerador_lotofacil():
    print("=====" * 16)
    print("===" * 8, "  GERADOR DE APOSTA LOTOFÁCIL  ", "===" * 8)
    print("=====" * 16)

    numero_jogos = int(input(">> Digite o número de jogos: "))
    jogo = 0
    resultado = []

    for linha in range(int(numero_jogos)):
        jogo += 1
        numeros = random.sample(range(1, 26), 15)

        for coluna in range(1):
            numeros = random.sample(range(1, 26), 15)
            print(f'>> Jogo {jogo}: ')
            print(numeros, end='')

        print()
        print("---" * 20)
        time.sleep(1)
        resultado.append(numeros)

    print("===" * 8, "Boa sorte!", "===" * 8)
    return resultado