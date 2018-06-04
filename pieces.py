from PyQt5.QtGui import *


class Piece:
    def __init__(self, row, column, board_info):
        self.r = row
        self.c = column
        self.board_info = board_info

    def draw(self, position_x, position_y):
        self.board_info.field_size_x = 0


class King(Piece):
    def draw(self, position_x, position_y):
        pass


class Queen(Piece):
    def draw(self, position_x, position_y):
        pass


class Bishop(Piece):
    def draw(self, position_x, position_y):
        pass


class Rook(Piece):
    def draw(self, position_x, position_y):
        pass


class Knight(Piece):
    def draw(self, position_x, position_y):
        pass


class Pawn(Piece):
    def draw(self, position_x, position_y):
        pawn_image = QPixmap("./Chess_plt45.png")
        self.board_info.painter.drawPixmap(position_x, position_y, 50, 50, pawn_image)
