import random

from const import *


class Board:
    def _randomInt(self):
        min = 0
        max = pow(2, 64)
        return random.randint(min, max)

    def __init__(self, board):
        self.board = board
        self.zobristTable = [[[self._randomInt() for k in range(NB_TYPE_PIECES)] for j in range(DIMENSION)] for i in range(DIMENSION)]
        self.hashValue = 0
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.board[i][j] != ES:
                    self.hashValue ^= self.zobristTable[i][j][self.board[i][j]]
    
    def move(self, x1, y1, x2, y2):
        """
        x1, y1 : start position
        x2, y2 : end position
        """
        self.board[x1][y1], self.board[x2][y2] = self.board[x2][y2], self.board[x1][y1]
        self.hashValue ^= self.zobristTable[x2][y2][self.board[x2][y2]]


if __name__ == "__main__":
    board = Board(ARD_RI_DISPOSITION)
    print(board.hashValue)
    board.move(0, 3, 1, 3)
    print(board.hashValue)