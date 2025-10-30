from .tabuleiro import *
from .gameconfigs import GameConfig
from .interface import alf,  ExibirTabuleiro
from .utils import *
from .styles import *

colors = Color()
def AdquirAcao(Tabuleiro: Tabuleiro, gameConfigs : GameConfig) -> str:
    """
    Retorna uma acao valida e formatada de acordo com todos os comando disponiveis
    """

    #Formatacao principal
    commandline = "Digite !help"
    if gameConfigs.command_mode != None:
        commandline = "Modo: " + str(gameConfigs.command_mode).upper()
    resposta = input(f"Comando ({commandline}): ")

    #Exucacao dos comandos
    match resposta:
        case "!help":
            print("\nCOMANDOS DISPONÍVEIS:\n")

            printc(colors.YELLOW, "ATENÇÃO:")
            print("  Antes de abrir ou marcar um quadrado, selecione um modo.")
            print("  Depois, digite a posição no formato: <linha><coluna>")
            print("  Exemplo: a0, j10, M5")
            print("  OBS: 'a10' é diferente de 'A10'!\n")

            printc(colors.GREEN,"MODOS DE JOGO:")
            print("  !mode           -> Mostra os modos disponíveis")
            print("  !mode abrir  ou !a  -> Muda para o modo de abrir")
            print("  !mode marcar ou !m  -> Muda para o modo de marcar\n")

            printc(colors.CYAN,"COMANDOS GERAIS:")
            print("  !ver        -> Mostra o tabuleiro atual")
            print("  !bandeiras  -> Mostra quantas bandeiras ainda restam")
            print("  !leave      -> Sair do jogo")

        case "!mode":
            print("\nPara alterar os modos, digite: ")
            print("  !mode abrir")
            print("  !mode marcar")
        
        case "!mode abrir":
            printc(colors.CYAN,"\nModo Alterado para Abrir...")
            gameConfigs.command_mode = "abrir"
        
        case "!a":
            printc(colors.CYAN,"\nModo Alterado para Abrir...")
            gameConfigs.command_mode = "abrir"

        case "!mode marcar":
            printc(colors.CYAN,"\nModo Alterado para Marcar...")
            gameConfigs.command_mode = "marcar"
        
        case "!m":
            printc(colors.CYAN,"\nModo Alterado para Marcar...")
            gameConfigs.command_mode = "marcar"

        case "!bandeiras":
            print(f"\nBandeiras: ({Tabuleiro.current_bandeiras}/{Tabuleiro.max_bandeiras})")

        case "!ver":
            print()
            ExibirTabuleiro(Tabuleiro)

        case "!leave":
            return "!leave"
        
        case _: #Tenta abrir uma posicao
            try:
                linha = alf.index(resposta[0])
                coluna = int(resposta[1:])
            except:
                print("Comando Inválido")
            else:
                if not PertenceAoTabuleiro(Tabuleiro, [linha, coluna]):
                    print("Posição Inválida")
                elif Tabuleiro.my_board[linha][coluna].aberto:
                    print("Essa posição já foi aberta!")
                elif Tabuleiro.my_board[linha][coluna].temBandeira and gameConfigs.command_mode == "abrir":
                    print("Essa posição tem uma bandeira!")
                else:
                    #Se não há nenhum modo e foi passado uma posição, é considerado para abarir
                    if gameConfigs.command_mode == None:
                        gameConfigs.command_mode = "abrir"
                    return([gameConfigs.command_mode,[linha,coluna]])
                
    return None
                    
        