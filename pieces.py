from PyQt5.QtGui import *


class Piece:
    def __init__(self, row, column, board_info):
        self.r = row
        self.c = column
        self.board_info = board_info

    def draw(self):
        self.board_info.field_size_x = 0


class King(Piece):
    def draw(self):
        pass


class Queen(Piece):
    def draw(self):
        pass


class Bishop(Piece):
    def draw(self):
        pass


class Rook(Piece):
    def draw(self):
        pass


class Knight(Piece):
    def draw(self):
        pass


class Pawn(Piece):
    def draw(self):
        pawn_image = QPixmap("./Chess_plt45.png")
        x, y = self.board_info.get_position(self.r, self.c)
        self.board_info.painter.drawPixmap(x, y, 99, 99, pawn_image)
