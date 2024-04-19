from board import Board
from constants import PLAYERS
from utils import WinGame, InvalidColumn, FullBoard


class Game:
    def __init__(self):
        self.board = Board()
        self.players = PLAYERS

    def start(self):
        print("Welcome to Connect 4 game!")
        try:
            while True:
                for player in self.players:
                    self.board.show_board()
                    try:
                        self.step(player)
                    except FullBoard as e:
                        raise e
        except WinGame as e:
            self.board.show_board()
            print(e)

    def step(self, player: str):
        self.board.check_full()

        while True:
            player_choice = input(f"Player {player}, please, select a column from (0-{self.board.col - 1}): ")
            if not player_choice.isdigit() or int(player_choice) < 0 or int(player_choice) >= self.board.col:
                print('Invalid input. Please choose a valid column.')
                continue
            else:
                try:
                    self.board.put_chip(int(player_choice), player)
                    break
                except WinGame as e:
                    raise e
                except InvalidColumn as e:
                    print(e)
                    continue
