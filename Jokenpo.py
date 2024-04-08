import random


def pessoa():
    d = int(input("Escolha sua jogada (digite Apenas o número correspondente):\n1. Pedra;\n2. Papel;\n3. Tesoura.\n"))
    if d in dec_possiveis:
        return d
    else:
        print("Escreva apenas 1, 2 ou 3 para selecionar sua jogada.")
        pessoa()


def computador():
    d = random.choice(dec_possiveis)
    return d


def resultado(pessoa, pc):
    if pessoa == pc:
        ganhador = "empate"
    elif pessoa == 1:
        if pc == 2:
            ganhador = "pc"
        else:
            ganhador = "pessoa"
    elif pessoa == 2:
        if pc == 1:
            ganhador = "pessoa"
        else:
            ganhador = "pc"
    else:
        if pc == 1:
            ganhador = "pc"
        else:
            ganhador = "pessoa"
    return ganhador


def ponto(ganhador):
    if ganhador == "empate":
        print("Foi um empate.")
    elif ganhador == "pessoa":
        print("Você ganhou.")
    else:
        print("Você perdeu.")


def jogo():
    pe = pessoa()
    pc = computador()
    pt = resultado(pe, pc)
    ponto(pt)


dec_possiveis = (1, 2, 3)
jogo()
