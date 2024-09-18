from tkinter import *
import random
from time import sleep


class Carta:
        def __init__(self, foto, nome):
                self.foto = foto
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
jacare = Carta('cartas\\jacare.png', 'Jacare')
leao = Carta('cartas\\leao.png', 'Leao')
lobo = Carta('cartas\\lobo.png', 'Lobo')
macaco = Carta('cartas\\macaco.png', 'Macaco')
passaro = Carta('cartas\\passaro.png', 'Passaro')
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
CARTAS = [cachorro, cavalo, coelho, coruja, elefante, gato, girafa, golfinho, jacare, leao, lobo, macaco, passaro, peixe, raposa, rato, sapo, tartaruga, tigre, urso, zebra]
PLAYERS = [player1, player2]
ROWS = 6
COLUMNS = 7

# variaveis
jogando = None
baralho = []
primeira_selecao = None
segunda_selecao = None


def new_game():
        global baralho, jogando, PLAYERS, CARTAS, ROWS, COLUMNS

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
        cartas = Frame(jogo)
        cartas.pack(side=BOTTOM)
        for linha in range(ROWS):
                for coluna in range(COLUMNS):
                        botao[linha][coluna] = Button(cartas, heigh = 4, width = 9, command = lambda: mostrar_carta(baralho[linha][coluna], buttons[linha][coluna])).grid(row = linha, column = coluna)


                        
def mostrar_carta(carta, botao):
        global primeira_selecao, segunda_selecao

        # fazer carta aparecer
        imagem = PhotoImage(file=carta.foto)  # configurar imagem
        botao.config(text = carta.nome, image = image, compound = 'top', heigh = 4, width = 9, bg = '#DDD', command = None)
        
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



jogo = Tk()

new_game()


jogo.mainloop()
# O QUE FAZER: terminar comparar_cartas() atualizando as pontuações e escondendo as cartas; configurar textos fora das funções
