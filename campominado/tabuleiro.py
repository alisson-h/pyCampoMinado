import random

class Bloco:
    """
    Representa cada bloco do tabuleiro
    """
    def __init__(self, aberto = False, temBomba = False, temBandeira = False, numero = 0):
        self.aberto = aberto
        self.temBomba = temBomba
        self.temBandeira = temBandeira
        self.numero = numero

class Tabuleiro:
    """
    Armazena o Tabuleiro e todas suas dependencias
    """

    def __init__(self, tam_linhas, tam_colunas, max_bombas = None, max_bandeiras = None, current_bandeiras = None):
        self.tam_linhas = tam_linhas
        self.tam_colunas = tam_colunas
        self.max_bombas = max_bombas
        self.max_bandeiras = max_bandeiras
        self.current_bandeiras = current_bandeiras
        
        self.my_board  = []
        
        for i in range(self.tam_linhas):
            self.my_board.append([])
            for j in range(tam_colunas):
                novoBloco = Bloco()
                self.my_board[i].append(novoBloco)

def CriarTabuleiro(MAX_TAM) -> Tabuleiro:
    """
        Inicializa um novo tabuleiro com dimensões a escolha do usario.
        Ao final retorna o novo tabuleiro
    """
    tam_linhas = 0
    tam_colunas = 0

    #Adquirindo o num de linhas
    while True:
        try:
            tam_linhas = int(input("Digite o numero de linhas: "))
        except:
            print("Dados Inválidos... Tente Novamente")
        else:
            if tam_linhas <= 1:
                print("Numero de linhas não pode ser menor que 2")
            elif tam_linhas > MAX_TAM:
                print(f"Numero de linhas não pode ser maior que {MAX_TAM}")
            else:
                break

    #Adquirindo o num de colunas
    while True:
        try:
            tam_colunas = int(input("Digite o numero de colunas: "))
        except:
            print("Dados Inválidos... Tente Novamente")
        else:
            if tam_colunas <= 1:
                print("Numero de colunas não pode ser menor que 2")
            elif tam_colunas > MAX_TAM:
                print(f"Numero de colunas não pode ser maior que {MAX_TAM}")
            else:
                break
    print()

    return Tabuleiro(tam_linhas, tam_colunas)

def InstanciarBombas(_Tabuleiro : Tabuleiro):
    """
    Instancia todas as bombas de forma aleatória no tabuleiro que recebe como parametro
    """

    #Garante que não há nenhuma bomba antes de iniciar o processo
    for i in range(_Tabuleiro.tam_linhas):
        for j in range(_Tabuleiro.tam_colunas):
            _Tabuleiro.my_board[i][j].temBomba = False

    #Instanciando bombas
    constBombas = 0
    while (constBombas < _Tabuleiro.max_bombas):
        nova_linha = random.randint(0,_Tabuleiro.tam_linhas - 1)
        nova_coluna = random.randint(0,_Tabuleiro.tam_colunas - 1)

        #Garantindo que não haja conflito nas posicoes das bombas
        if not _Tabuleiro.my_board[nova_linha][nova_coluna].temBomba:
            _Tabuleiro.my_board[nova_linha][nova_coluna].temBomba = True
            constBombas += 1

