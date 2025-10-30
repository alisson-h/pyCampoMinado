from .tabuleiro import *
from .interface import *
from .commands import *
from .utils import *
from .gameconfigs import *

from math import ceil

MAX_TAM = 50

def RealizarAcao(Tabuleiro: Tabuleiro, gameConfigs : GameConfig):
    """
    Realiza uma função de acordo com a escolha do Usuario
    """

    #Adquirir a acao do Usuario
    Acao = None
    while Acao == None:
        Acao = AdquirAcao(Tabuleiro, gameConfigs)
        print()
    
    # Todas as acoes possiveis:
    # ---------------------------

    if Acao == "!leave": #Sair da aplicacao
        return False
    
    match Acao[0]:
        case "abrir": #Abrir uma casa
            gameConfigs.rodadas += 1

            #Se for sua primeira vez abrindo uma celula, garante que não seja aberto uma bomba
            #Se possivel também garente que seja aperto uma celula com numero 1
            if gameConfigs.rodadas == 1:
                while Tabuleiro.my_board[Acao[1][0]][Acao[1][1]].temBomba or (Tabuleiro.my_board[Acao[1][0]][Acao[1][1]].numero != 0 and Tabuleiro.tam_colunas * Tabuleiro.tam_linhas > 4):
                    InstanciarBombas(Tabuleiro)
                    ConfigurarNumeracao(Tabuleiro)

            AbrirApartirDasPosições(Tabuleiro, [Acao[1]])

        case "marcar": #Marcar / Desmarcar um posicao 
            Marcar = MarcarPosição(Tabuleiro, Acao[1])
            if Marcar:
                print(f"Bandeiras Restantes: {Tabuleiro.current_bandeiras}")
            else:
                print("Você já usou todas as suas bandeiras!")
        case _:
            print("Ação Inválida")
            RealizarAcao(Tabuleiro)
    
    return True
            
def iniciarCampoMinado():
    """
        Responsável por Inicializar o Campo Minado.
        É aquirido o tamanho do tabuleiro, quantidade de bombas, e o loop principal
    """
    print("\n--- Seja Bem Vindo ao Campo Minado! ---\n")
    print("Escolha a quantidade das colunas e linhas (entre 2 e 50)\n")

    #Cria o Tabuleiro de acordo com o tamanho fornecido pelo Usuario
    novoTabuleiro = CriarTabuleiro(MAX_TAM)
    #Escolhe a dificuldade de acordo com a escolha do Usuario
    novaGameConfig = GameConfig(DefinirDificuldade(novoTabuleiro))
    print()

    #Define o maximo de bombas
    novoTabuleiro.max_bombas = ceil(novoTabuleiro.tam_linhas * novoTabuleiro.tam_colunas * novaGameConfig.dificuldade.value)
    novoTabuleiro.max_bombas = novoTabuleiro.max_bandeiras = novoTabuleiro.current_bandeiras = novoTabuleiro.max_bombas

    #Adciona as bombas no tabuleiro e atualiza todas as nummracoes
    InstanciarBombas(novoTabuleiro)
    ConfigurarNumeracao(novoTabuleiro)
    
    #Loop principal do jogo
    jogando = True
    while jogando:
        ExibirTabuleiro(novoTabuleiro)

        #Acao do Usuario
        jogando = RealizarAcao(novoTabuleiro, novaGameConfig)
        if not jogando:
            break

        #Verifica estado do jogo (Vitoria / Derrota)
        perdeu = VerificarDerrota(novoTabuleiro)

        if (perdeu):
            jogando = False
            ExibirTabuleiro(novoTabuleiro)
            print("\n -> Putz! Achou uma bomba :( \n")

        ganhou = VerificarVitoria(novoTabuleiro)
        if (ganhou):
            jogando = False
            ExibirTabuleiro(novoTabuleiro)
            print("\n -> Parábens! Você encontrou todas as bombas")

    return