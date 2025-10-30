class Color():
    """
    Armazena cores baseadas na tabela ANSI
    """
    def __init__(self):
        self.RED = "\033[31m"
        self.GREEN = "\033[32m"
        self.darkGREEN = "\033[2m\033[92m"
        self.YELLOW = "\033[33m"
        self.BLUE = "\033[34m"
        self.MAGENTA = "\033[35m"
        self.CYAN = "\033[36m"
        self.WHITE = "\033[37m"
        self.END = "\033[0m"

def printc(color, text):
    """
    Imprime o texto com a cor informada
    """
    print(f"{color}{text}{Color().END}")