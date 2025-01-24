''' This is the main logic for a Tic-tac-toe game.
It is not optimised for a quality game it simply
generates random moves and checks the results of
a move for a winning line. Exposed functions are:
newGame()
saveGame()
restoreGame()
userMove()
computerMove()
'''

import os, random
import oxo_data

class Game:
    def __init__(self):
        self.board = [" "] * 9

    def new_game(self):
        self.board = [" "] * 9
        return self.board

    def save_game(self, filename="oxogame.dat"):
        with open(filename, "w") as file:
            file.write("".join(self.board))

    def restore_game(self, filename="oxogame.dat"):
        try:
            with open(filename, "r") as file:
                self.board = list(file.read().strip())
        except FileNotFoundError:
            self.new_game()
        return self.board

    def user_move(self, cell):
        if self.board[cell] == " ":
            self.board[cell] = "X"
            return self.is_winning_move()
        return "Invalid move"

    def computer_move(self):
        from random import choice
        available_cells = [i for i, cell in enumerate(self.board) if cell == " "]
        if available_cells:
            move = choice(available_cells)
            self.board[move] = "O"
            return self.is_winning_move()
        return "Draw"

    def is_winning_move(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)             # Diagonals
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != " ":
                return self.board[a]
        return ""

    def test(self):
        result = ""
        while not result:
            print(self.board)
            try:
                result = self.user_move(random.choice([i for i in range(9) if self.board[i] == " "]))
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computer_move()

            if not result:
                continue
            elif result == 'D':
                print("It's a draw")
            else:
                print("Winner is:", result)
            print(self.board)

if __name__ == "__main__":
    game = Game()
    game.test()


            
