from tkinter import *
import random
from time import sleep


jogo = Tk()


class Carta:
    def __init__(self, foto, nome):
        self.foto = PhotoImage(file=foto)
        self.nome = nome


class Player:
    def __init__(self, cor):
        self.cor = cor
        self.pontos = 0


# criando cartas
cachorro = Carta('cartas\\cachorro.png', 'Cachorro')
cavalo = Carta('cartas\\cavalo.png', 'Cavalo')
coelho = Carta('cartas\\coelho.png', 'Coelho')
coruja = Carta('cartas\\coruja.png', 'Coruja')
elefante = Carta('cartas\\elefante.png', 'Elefante')
gato = Carta('cartas\\gato.png', 'Gato')
girafa = Carta('cartas\\girafa.png', 'Girafa')
golfinho = Carta('cartas\\golfinho.png', 'Golfinho')
jacare = Carta('cartas\\jacare.png', 'Jacaré')
leao = Carta('cartas\\leao.png', 'Leão')
lobo = Carta('cartas\\lobo.png', 'Lobo')
macaco = Carta('cartas\\macaco.png', 'Macaco')
passaro = Carta('cartas\\passaro.png', 'Pássaro')
peixe = Carta('cartas\\peixe.png', 'Peixe')
raposa = Carta('cartas\\raposa.png', 'Raposa')
rato = Carta('cartas\\rato.png', 'Rato')
sapo = Carta('cartas\\sapo.png', 'Sapo')
tartaruga = Carta('cartas\\tartaruga.png', 'Tartaruga')
tigre = Carta('cartas\\tigre.png', 'Tigre')
urso = Carta('cartas\\urso.png', 'Urso')
zebra = Carta('cartas\\zebra.png', 'Zebra')

# criando players
player1 = Player('#0000FF')
player2 = Player('#FF0000')

# constantes
CARTAS = [cachorro, cavalo, coelho, coruja, elefante, gato, girafa, golfinho, jacare, leao, lobo, macaco, passaro,
          peixe, raposa, rato, sapo, tartaruga, tigre, urso, zebra]
PLAYERS = [player1, player2]
ROWS = 6
COLUMNS = 7

# variaveis
jogando = None
baralho = []
primeira_selecao = None
segunda_selecao = None
buttons = [['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '']]


def new_game():
    global baralho, jogando, PLAYERS, CARTAS, ROWS, COLUMNS, cartas

    # reiniciar pontuações
    for player in PLAYERS:
        player.pontos = 0

    # randomizar primeiro player
    jogando = random.choice(PLAYERS)

    # embaralhar
    baralho = []  # resetar baralho
    possibilidades = CARTAS * 2  # todas as cartas para embaralhar
    for linha in range(ROWS):
        temp = []  # variável para armazenar cada linha
        for coluna in range(COLUMNS):
            card = random.choice(possibilidades)  # carta aleatória possível
            temp.append(card)  # colocar na linha
            possibilidades.remove(card)  # tirar das possibilidades
        baralho.append(temp)  # armazenar linha no baralho

    # configurar na janela
    cartas.grid()
    for linha in range(ROWS):
        for coluna in range(COLUMNS):
            buttons[linha][coluna] = Button(cartas, height=4, width=9,
                                          command=lambda: mostrar_carta(baralho[linha][coluna],
                                                                        linha, coluna))
            buttons[linha][coluna].grid(row=linha, column=coluna)


def mostrar_carta(carta, linha, coluna):
    global primeira_selecao, segunda_selecao, cartas

    # fazer carta aparecer
    buttons[linha][coluna].config(text=carta.nome, image=carta.foto, compound='top')
    buttons[linha][coluna].grid(row=linha, column=coluna)
    cartas.grid()


    # configurar seleção
    if primeira_selecao != None:
        primeira_selecao = carta.nome
    else:
        segunda_selecao = carta.nome
        comparar_cartas()


def comparar_cartas():
    global primeira_selecao, segunda_selecao, jogando, PLAYERS

    # comparar cartas
    if primeira_selecao == segunda_selecao:
        jogando.pontos += 1
    else:
        pass


cartas = Frame(jogo)
new_game()

jogo.mainloop()

