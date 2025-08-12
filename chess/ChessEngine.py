class GameState():
    def __init__(self):
        #tabuleiro 8x8, cada
        self.board = [
            []
        ]
        self.whiteToMove = True
        self.moveLog = []