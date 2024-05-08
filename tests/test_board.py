import unittest
import random
import string
from board import Board
from constants import PLAYERS, NUM_COL, NUM_ROW, WIN_NUM
from utils import InvalidColumn, WinGame, FullBoard


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = random.choice(PLAYERS)

    def _get_random_player(self) -> string:
        return random.choice(string.ascii_uppercase)

    def test_put_chip(self):
        for i in range(NUM_COL):
            player = self._get_random_player()
            self.board.put_chip(i, player)
            self.assertEqual(self.board.board[NUM_ROW - 1][i], player)

    def test_invalid_column(self):
        with self.assertRaises(InvalidColumn):
            self.board.put_chip(-1, self._get_random_player())
            self.board.put_chip(NUM_COL, self._get_random_player())

    def test_full_column(self):
        col = random.randint(0, NUM_COL - 1)
        for _ in range(NUM_ROW):
            self.board.put_chip(col, self._get_random_player())

        with self.assertRaises(InvalidColumn):
            self.board.put_chip(col, self._get_random_player())

    def test_win_game(self):
        col = random.randint(0, NUM_COL - 1)
        for _ in range(WIN_NUM - 1):
            self.board.put_chip(col, self.player)
        with self.assertRaises(WinGame):
            self.board.put_chip(col, self.player)

    def test_full_board(self):
        for col in range(NUM_COL):
            for _ in range(NUM_ROW):
                self.board.put_chip(col, self._get_random_player())
        with self.assertRaises(FullBoard):
            self.board.check_full()
