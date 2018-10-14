from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtSvg import *


class Piece:
    def __init__(self, row, column, board_info):
        self.r = row - 1
        self.c = column - 1
        self.board_info = board_info

    def draw(self):
        self.board_info.field_size_x = 0

    def draw_picture(self, filename):
        board = self.board_info
        renderer = QSvgRenderer(filename)
        picture_map = QPixmap(board.field_size_x, board.field_size_y);
        picture_map.fill(Qt.transparent)
        painter = QPainter(picture_map)
        painter.begin(picture_map)
        renderer.render(painter)
        painter.end()
        piece_image = QPixmap(picture_map)  # Maybe preload it to list of images
        x, y = board.get_position(self.r, self.c)
        board.painter.drawPixmap(x, y, board.field_size_x, board.field_size_y, piece_image)


class King(Piece):
    def draw(self):
        self.draw_picture("./Chess_klt45.svg")


class Queen(Piece):
    def draw(self):
        self.draw_picture("./Chess_qlt45.svg")


class Bishop(Piece):
    def draw(self):
        self.draw_picture("./Chess_blt45.svg")


class Rook(Piece):
    def draw(self):
        self.draw_picture("./Chess_rlt45.svg")


class Knight(Piece):
    def draw(self):
        self.draw_picture("./Chess_nlt45.svg")


class Pawn(Piece):
    def draw(self):
        self.draw_picture("./Chess_plt45.svg")

