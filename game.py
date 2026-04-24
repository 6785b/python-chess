from board import Board, Move
from figures import *

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'white'
        self.game_over = False

    def start(self):
        for col in range(8):
            self.board.place_figure(6, col, Pawn('P', 'white', 6, col))
            self.board.place_figure(1, col, Pawn('p', 'black', 1, col))

        self.board.place_figure(7, 0, Rook('R','white',7,0))
        self.board.place_figure(7, 7, Rook('R','white',7,7))
        self.board.place_figure(7, 1, Knight('N','white',7,1))
        self.board.place_figure(7, 6, Knight('N','white',7,6))
        self.board.place_figure(7, 2, Bishop('B','white',7,2))
        self.board.place_figure(7, 5, Bishop('B','white',7,5))
        self.board.place_figure(7, 3, Queen('Q','white',7,3))
        self.board.place_figure(7, 4, King('K','white',7,4))

        self.board.place_figure(0, 0, Rook('r','black',0,0))
        self.board.place_figure(0, 7, Rook('r','black',0,7))
        self.board.place_figure(0, 1, Knight('n','black',0,1))
        self.board.place_figure(0, 6, Knight('n','black',0,6))
        self.board.place_figure(0, 2, Bishop('b','black',0,2))
        self.board.place_figure(0, 5, Bishop('b','black',0,5))
        self.board.place_figure(0, 3, Queen('q','black',0,3))
        self.board.place_figure(0, 4, King('k','black',0,4))

    def switch_turn(self):
        self.turn = 'black' if self.turn == 'white' else 'white'

    def parse_position(self, pos):
        col_letters = "abcdefgh"
        col = col_letters.index(pos[0])
        row = 8 - int(pos[1])
        return row, col

    def play(self):
        while not self.game_over:
            self.board.print_board()
            print("Ходят:", self.turn)

            move_input = input("Впиши ход(пример: e2 e4): ")

            try:
                s, e = move_input.split()
            except:
                print("Ошибка ввода")
                continue

            sr, sc = self.parse_position(s)
            er, ec = self.parse_position(e)

            figure = self.board.get_figure(sr, sc)

            if not figure or figure.color != self.turn:
                print("Нельзя ходить")
                continue

            moves = figure.get_possible_moves(self.board.board)

            if (er, ec) not in moves:
                print("Недопустимый ход")
                continue

            self.board.board[er][ec] = figure
            self.board.board[sr][sc] = None
            figure.update_position(er, ec)

            self.switch_turn()


if __name__ == "__main__":
    game = Game()
    game.start()
    game.play()
    