"""
Codigos com funcoes uteis para o jogo da velha
"""
from .tabuleiro import Tabuleiro


percorrer = [[-1,-1], [-1, 0], [-1, 1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

def PertenceAoTabuleiro(Tabuleiro :Tabuleiro, Posicao) -> bool:
    """Verifica se uma posicao pertence ao tabuleiro e retorna o resultado"""
    return Posicao[0] >= 0 and Posicao[0] < Tabuleiro.tam_linhas and Posicao[1] >= 0 and Posicao[1] < Tabuleiro.tam_colunas
    
def ConfigurarNumeracao(Tabuleiro :Tabuleiro):
    """Configura a numeracao de bombas do tabuleiro"""
    for i in range(Tabuleiro.tam_linhas):
        for j in range(Tabuleiro.tam_colunas):
            soma = 0
            for posicao in percorrer:
                contarLinha = i + posicao[0]
                contarColuna = j + posicao[1]
                if PertenceAoTabuleiro(Tabuleiro, [contarLinha, contarColuna]):
                    if (Tabuleiro.my_board[contarLinha][contarColuna].temBomba):
                        soma += 1
            Tabuleiro.my_board[i][j].numero = soma

def MarcarPosição(Tabuleiro :Tabuleiro, Posicao):
    """Acao de marcar/desmarcar uma casa dada uma posicao"""
    
    if Tabuleiro.my_board[Posicao[0]][Posicao[1]].temBandeira:
        #Desmarcar
        Tabuleiro.current_bandeiras += 1
        Tabuleiro.my_board[Posicao[0]][Posicao[1]].temBandeira = False

        return True
    else:
        #Marcar se houver bandeiras disponiveis
        if Tabuleiro.current_bandeiras > 0:
            Tabuleiro.current_bandeiras -= 1
            Tabuleiro.my_board[Posicao[0]][Posicao[1]].temBandeira = True

            return True
        else:
            return False

def AbrirApartirDasPosições(Tabuleiro : Tabuleiro, ListaPosicoes):
    """
    Funcao Recursica que dada uma lista de posicoes:
        - Percorre todas as posicoes fornecidas:
            - Abre essa posicao;
            - Se o numero dessa casa for 0, armazena todas as casas adjacente que podem ser abertas
            a uma nova lista de posicoes.
    Ao final chama a funcao novamente. Agora, com a nova lista de posicoes para serem abertas
    """
    novaListaPosicoes = []
    for EstaPosicao in ListaPosicoes:
        if(not Tabuleiro.my_board[EstaPosicao[0]][EstaPosicao[1]].aberto):
            Tabuleiro.my_board[EstaPosicao[0]][EstaPosicao[1]].aberto = True
            if Tabuleiro.my_board[EstaPosicao[0]][EstaPosicao[1]].numero == 0 and not Tabuleiro.my_board[EstaPosicao[0]][EstaPosicao[1]].temBomba:
                for posicao in percorrer:
                    contarLinha = EstaPosicao[0] + posicao[0]
                    contarColuna = EstaPosicao[1] + posicao[1]
                    if PertenceAoTabuleiro(Tabuleiro, [contarLinha, contarColuna]):
                        if (not Tabuleiro.my_board[contarLinha][contarColuna].aberto and not Tabuleiro.my_board[contarLinha][contarColuna].temBandeira):
                            if [contarLinha, contarColuna] not in novaListaPosicoes:
                                novaListaPosicoes.append([contarLinha, contarColuna])

                AbrirApartirDasPosições(Tabuleiro, novaListaPosicoes)

def VerificarVitoria(Tabuleiro : Tabuleiro) -> bool:
    """
    Verifica se todas as bandeiras marcam todas as bombas corretamente e retorna esse resultado
    """

    #Se todas as bandeiras ainda não foram posicionadas, não há como o Usuario vencer o jogo
    if Tabuleiro.current_bandeiras > 0:
        return False
    
    bandeira_corretas = 0
    for i in range(Tabuleiro.tam_linhas):
        for j in range(Tabuleiro.tam_colunas):
            if Tabuleiro.my_board[i][j].temBomba and Tabuleiro.my_board[i][j].temBandeira:
                bandeira_corretas += 1 
    
    return bandeira_corretas == Tabuleiro.max_bandeiras

def VerificarDerrota(Tabuleiro : Tabuleiro) -> bool:
    """
    Verifica se há alguma bomba aberta e retorna esse resultado
    """
    for i in range(Tabuleiro.tam_linhas):
        for j in range(Tabuleiro.tam_colunas):
            if Tabuleiro.my_board[i][j].temBomba and Tabuleiro.my_board[i][j].aberto:
                return True
    return False