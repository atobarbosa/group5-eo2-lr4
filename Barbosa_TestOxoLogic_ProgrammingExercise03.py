import unittest
from oxo_logic import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.new_game()

    def test_new_game(self):
        self.assertEqual(self.game.board, [" "] * 9)

    def test_user_move_valid(self):
        self.game.user_move(0)
        self.assertEqual(self.game.board[0], "X")

    def test_user_move_invalid(self):
        self.game.user_move(0)
        result = self.game.user_move(0)
        self.assertEqual(result, "Invalid move")

    def test_computer_move(self):
        self.game.computer_move()
        self.assertIn("O", self.game.board)

    def test_is_winning_move(self):
        self.game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        result = self.game.is_winning_move()
        self.assertEqual(result, "X")

if __name__ == "__main__":
    unittest.main()