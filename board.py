class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.eaten_figures = []
        self.move_log = []

    def get_figure(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        else:
            print('Недопустимые координаты')

    def place_figure(self, row, col, figure):
        if 0 <= row < 8 and 0 <= col < 8 and self.board[row][col] is None:
            self.board[row][col] = figure
        else:
            print('Недопустимый ход')

    def print_board(self):
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            line = []
            for cell in row:
                line.append("." if cell is None else cell.symbol)
            print(8 - i, " ".join(line), 8 - i)


class Move:
    def __init__(self, start_row, start_col, end_row, end_col, moved_piece, captured_piece):
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col
        self.moved_piece = moved_piece
        self.captured_piece = captured_piece