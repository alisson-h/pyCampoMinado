from .tabuleiro import *
from .utils import *
from .styles import *

frasesSair = ["sair", "leave", "kit", "out", "l", "k"]

alf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
       "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

colors = Color()
def ExibirTabuleiro(_Tabuleiro : Tabuleiro):
        """Exibe o tabuleiro do jogo formatado"""

        for i in range(-1, _Tabuleiro.tam_linhas):
            if i == 0: print()
            for j in range(-1, _Tabuleiro.tam_colunas):
                if j == 0: 
                    print(" ", end ="")

                caracter = "*"
                if i == -1 and j == -1:
                     caracter = " "
                elif i == -1:
                     caracter = j
                elif j == -1:
                     caracter = alf[i]
                elif _Tabuleiro.my_board[i][j].aberto and not _Tabuleiro.my_board[i][j].temBomba:
                    caracter = _Tabuleiro.my_board[i][j].numero
                    if caracter == 0: caracter = " "
                elif _Tabuleiro.my_board[i][j].aberto and _Tabuleiro.my_board[i][j].temBomba:
                    caracter = "B"
                elif _Tabuleiro.my_board[i][j].temBandeira:
                    caracter = "M"
                
                if j >= 0 and i >=0:
                    match caracter:
                        case "*":
                            if (i + j) % 2 == 0:
                                print(colors.darkGREEN, end = "")
                            else:
                                print(colors.GREEN, end = "")
                        case "M":
                            print(colors.RED, end = "")
                        case 1:
                            print(colors.CYAN, end = "")
                        case 2:
                            print(colors.RED, end = "")    
                        case 3:
                            print(colors.MAGENTA, end = "")
                        case 4:
                            print(colors.BLUE, end = "")
                        case 5:
                            print(colors.YELLOW, end = "")

                print(f"{caracter:>3}", end = "")
                print(colors.END, end = "")
                
            print()
        print()

