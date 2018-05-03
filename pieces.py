class Piece:
    def __init__(self, row, column, board_info):
        self.r = row
        self.c = column
        self.board_info = board_info

    def draw(self, canvas, position_x, position_y):
        self.board_info.field_size_x = 0


class King(Piece):
    def draw(self, canvas, position_x, position_y):
        pass


class Queen(Piece):
    def draw(self, canvas, position_x, position_y):
        pass


class Bishop(Piece):
    def draw(self, canvas, position_x, position_y):
        pass


class Rook(Piece):
    def draw(self, canvas, position_x, position_y):
        pass


class Knight(Piece):
    def draw(self, canvas, position_x, position_y):
        pass


class Pawn(Piece):
    def draw(self, canvas, position_x, position_y):
        canvas.create_rectangle(position_x,
                                position_y,
                                position_x + self.board_info.field_size_x - 20,
                                position_y + self.board_info.field_size_y - 20, fill="cornsilk2")
