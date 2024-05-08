import unittest
from io import StringIO
from unittest.mock import patch

from constants import PLAYERS
from game import Game
from utils import WinGame, FullBoard


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.win_player = PLAYERS[0]

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input',
           side_effect=['0', '1', '0', '1', '0', '1', '0'])
    def test_game_start(self, mock_input, mock_output):
        # with self.assertRaises(WinGame):
        self.game.start()
        self.assertEqual(mock_output.getvalue()[-17:], f"Player {self.win_player} is win!\n")
