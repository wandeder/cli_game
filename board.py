from constants import NUM_ROW, NUM_COL, EMPTY_CELL, WIN_NUM
from utils import WinGame, InvalidColumn, FullBoard


class Board:
    """Representig game board"""
    def __init__(self):
        self.row = NUM_ROW
        self.col = NUM_COL
        self.empty_cell = EMPTY_CELL
        self.win_num = WIN_NUM
        self.board = self._get_empty_board()
        self.delta = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]

    def _get_empty_board(self):
        return [[self.empty_cell for _ in range(self.col)] for _ in range(self.row)]

    def show_board(self):
        for i in range(self.row):
            print(" ".join(self.board[i]))
        print(" ".join([str(x) for x in range(self.col)]))

    def put_chip(self, col: int, player: str):
        if col < 0 or col >= self.col:
            raise InvalidColumn("Invalid column")

        for row in range(self.row - 1, -1, -1):
            if self.board[row][col] == self.empty_cell:
                self.board[row][col] = player
                self.check_win_cell(row, col, player)
                return

        raise InvalidColumn("Column is full, cannot drop a chip here")

    def check_win_cell(self, row: int, col: int, player: str) -> None:
        """Check win conditional for all directions"""
        for delta_row, delta_col in self.delta:
            if self._check_win(row, col, delta_row, delta_col, player):
                raise WinGame(f"Player {player} is win!")

    def _check_win(self, row: int, col: int, delta_row: int, delta_col: int, player:str):
        for _ in range(self.win_num -1):
            row += delta_row
            col += delta_col
            if (
                    row < 0
                    or row >= self.row - 1
                    or col < 0
                    or col >= self.col - 1
                    or self.board[col][row] != player
            ):
                return False
        return True

    def check_full(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == self.empty_cell:
                    return
        raise FullBoard("The board is full! Stop the game")
