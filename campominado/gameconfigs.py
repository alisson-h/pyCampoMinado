from enum import Enum
from .tabuleiro import Tabuleiro
from .styles import *

import math

colors = Color()
class Dificuldade(Enum):
    facil = 0.1
    media = 0.2
    dificil =  0.3

class GameConfig():
    """Configuracoes gerais do jogo"""
    def __init__(self, dificuldade : Dificuldade ):
        self.dificuldade = dificuldade
        self.command_mode = None
        self.rodadas = 0

def AdquirirTextoBombas(_Tabuleiro : Tabuleiro, diff : Dificuldade):
    num = math.ceil(_Tabuleiro.tam_linhas * _Tabuleiro.tam_colunas * diff.value)
    if num == 1:
        return str(num) + " Bomba"
    return str(num) + " Bombas"

def DefinirDificuldade(_Tabuleiro : Tabuleiro) -> Dificuldade:
    """Adquire a dificuldade ao jogo baseado na escolha do usuario.
    Ao final, retora a dificuldade escolhida"""
    
    print("Defina a dificuldade do jogo:")
    print(f"F. {colors.GREEN}Fácil{colors.END}    :  {AdquirirTextoBombas(_Tabuleiro, Dificuldade.facil)}")
    print(f"M. {colors.YELLOW}Médio{colors.END}    :  {AdquirirTextoBombas(_Tabuleiro, Dificuldade.media)}")
    print(f"D. {colors.RED}Difícil{colors.END}  :  {AdquirirTextoBombas(_Tabuleiro, Dificuldade.dificil)}")

    respDificuldade = ""
    while True:
        try:
            respDificuldade = str(input("Resposta: "))
        except:
            print("Dados inválidos... tente novamente")
        else:
            match respDificuldade.upper():
                case "F":
                    return Dificuldade.facil
                case "M":
                    return Dificuldade.media
                case "D":
                    return Dificuldade.dificil
                case _:
                    print("Dificuldade não encontrada... tente novamente")