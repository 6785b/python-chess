class Figure:
    def __init__(self, symbol, color, row, col):
        self.color = color
        self.symbol = symbol
        self.position = (row, col)

    def update_position(self, row, col):
        self.position = (row, col)


class Rook(Figure):
    def get_possible_moves(self, board):
        moves = []
        row, col = self.position
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for dr, dc in directions:
            i = 1
            while True:
                r = row + dr*i
                c = col + dc*i
                if not (0 <= r < 8 and 0 <= c < 8):
                    break
                cell = board[r][c]
                if cell is None:
                    moves.append((r, c))
                elif cell.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
                i += 1
        return moves


class Bishop(Figure):
    def get_possible_moves(self, board):
        moves = []
        row, col = self.position
        directions = [(1,1),(-1,1),(1,-1),(-1,-1)]

        for dr, dc in directions:
            i = 1
            while True:
                r = row + dr*i
                c = col + dc*i
                if not (0 <= r < 8 and 0 <= c < 8):
                    break
                cell = board[r][c]
                if cell is None:
                    moves.append((r, c))
                elif cell.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
                i += 1
        return moves


class Knight(Figure):
    def get_possible_moves(self, board):
        moves = []
        row, col = self.position
        directions = [(2,1),(1,2),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

        for dr, dc in directions:
            r = row + dr
            c = col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                cell = board[r][c]
                if cell is None or cell.color != self.color:
                    moves.append((r, c))
        return moves


class Queen(Figure):
    def get_possible_moves(self, board):
        return Rook.get_possible_moves(self, board) + Bishop.get_possible_moves(self, board)


class King(Figure):
    def get_possible_moves(self, board):
        moves = []
        row, col = self.position
        directions = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

        for dr, dc in directions:
            r = row + dr
            c = col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                cell = board[r][c]
                if cell is None or cell.color != self.color:
                    moves.append((r, c))
        return moves


class Pawn(Figure):
    def __init__(self, symbol, color, row, col):
        super().__init__(symbol, color, row, col)
        self.has_moved = False

    def get_possible_moves(self, board):
        moves = []
        row, col = self.position
        direction = -1 if self.color == "white" else 1

        # вперед
        if board[row + direction][col] is None:
            moves.append((row + direction, col))

            if not self.has_moved and board[row + 2*direction][col] is None:
                moves.append((row + 2*direction, col))

        # атаки
        for dc in [-1, 1]:
            r = row + direction
            c = col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = board[r][c]
                if target and target.color != self.color:
                    moves.append((r, c))

        return moves