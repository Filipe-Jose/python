from tkinter import *
import random


jogo = Tk()
jogo.title('Jogo da Memória')

menu = Frame(jogo)
placar = Frame(menu)
cartas = Frame(jogo)


class Carta:
    def __init__(self, foto, nome):
        self.foto = PhotoImage(file=foto).subsample(3, 3).zoom(2, 2)
        self.nome = nome


class Player:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.pontos = 0
        self.label = Label(placar, text=(f'{self.nome}: {self.pontos}'), font=('Consolas', 12), fg=self.cor, padx = 100)
        self.text = lambda: str(f'{self.nome}: {self.pontos}')
    

class Selecao:
    def __init__(self, label, linha, coluna, animal):
        self.label = label
        self.linha = linha
        self.coluna = coluna
        self.animal = animal


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
player1 = Player('Player 1', '#0000FF')
player2 = Player('Player 2', '#FF0000')

# constantes
CARTAS = [cachorro, cavalo, coelho, coruja, elefante, gato, girafa, golfinho, jacare, leao, lobo, macaco, passaro,
          peixe, raposa, rato, sapo, tartaruga, tigre, urso, zebra]
PLAYERS = [player1, player2]
ROWS = 6
COLUMNS = 7

# variaveis
labels = []
jogando = None
baralho = []
primeira = Selecao(None, None, None, None)
segunda = Selecao(None, None, None, None)
buttons = [['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '']]


def new_game():
    global baralho, jogando, PLAYERS, CARTAS, ROWS, COLUMNS, cartas, primeira, segunda, labels

    # reiniciar pontuações
    for player in PLAYERS:
        player.pontos = 0

    # reiniciar tela
    for i in labels:
        i.destroy()

    # reiniciar selecoes
    primeira.label = None

    # randomizar primeiro player
    jogando = random.choice(PLAYERS)
    alternar_jogador()

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
    cartas.pack(side='bottom')
    for linha in range(ROWS):
        for coluna in range(COLUMNS):
            buttons[linha][coluna] = Button(cartas, height = 6, width = 12, command = lambda l = linha, c = coluna: mostrar_carta(baralho[l][c], l, c))
            buttons[linha][coluna].grid(row=linha, column=coluna)


def mostrar_carta(carta, linha, coluna):
    global primeira, segunda, cartas

    # fazer botão desaparecer
    buttons[linha][coluna].grid_forget()

    # configurar seleção e mostra carta
    if primeira.animal is None:
        primeira.animal = carta
        primeira.linha = linha
        primeira.coluna = coluna
        primeira.label = Label(cartas, text=carta.nome, image=carta.foto, compound='top', font=('Consolas', 12))
        primeira.label.grid(row = linha, column = coluna)
    else:
        segunda.animal = carta
        segunda.linha = linha
        segunda.coluna = coluna
        segunda.label = Label(cartas, text=carta.nome, image=carta.foto, compound='top', font=('Consolas', 12))
        segunda.label.grid(row = linha, column = coluna)
        igual = comparar_cartas()
      

def comparar_cartas():
    global primeira, segunda, jogando, PLAYERS

    desabilitar_botoes()
    
    # comparar cartas
    if primeira.animal == segunda.animal:  # se acertou
        jogando.pontos += 1
        atualizar_placar()
        primeira.label.config(bd = 2, bg = jogando.cor)  # mudar cor do fundo e colocar borda
        segunda.label.config(bd = 2, bg = jogando.cor)

        # guardar labels para apagar dps
        labels.append(primeira.label)
        labels.append(segunda.label)

        primeira.animal = None
        segunda.animal = None
        reabilitar_botoes()
    else:
        cartas.after(2000, esconder_cartas)

    
def desabilitar_botoes():
    global ROWS, COLUMNS, buttons

    for linha in range(ROWS):
        for coluna in range(COLUMNS):
            buttons[linha][coluna].config(state='disabled')


def reabilitar_botoes():
    global ROWS, COLUMNS, buttons
    
    for linha in range(ROWS):
        for coluna in range(COLUMNS):
            if buttons[linha][coluna]:  # Verifica se o botão ainda existe
                buttons[linha][coluna].config(state='normal')        


def alternar_jogador():
    global player1, player2, jogando, turno

    if jogando == player1:
            jogando = player2
    else:
            jogando = player1
    
    atualizar_placar()


def esconder_cartas():
    global primeira, segunda, jogando

    primeira.label.destroy()
    primeira.label = None
    primeira.animal = None
    buttons[primeira.linha][primeira.coluna].grid(row = primeira.linha, column = primeira.coluna)

    segunda.label.destroy()
    segunda.label = None
    segunda.animal = None
    buttons[segunda.linha][segunda.coluna].grid(row = segunda.linha, column = segunda.coluna)

    alternar_jogador()
    reabilitar_botoes()
    

def atualizar_placar():
    global PLAYERS, jogando, turno

    for i in PLAYERS:
        i.label.config(text=i.text())
        i.label.pack()

    jogo.config(background=jogando.cor)


placar.pack(side='left')
menu.pack(side='top')
Button(menu, text='Embaralhar', font=('Consolas', 12), command=new_game).pack(side='right')
new_game()

jogo.mainloop()
