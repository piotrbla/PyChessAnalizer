from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtSvg import *


class Piece:
    def __init__(self, row, column, board_info, color):
        self.r = row - 1
        self.c = column - 1
        self.board_info = board_info
        self.color = color
        self.filename = ""

    def draw(self):
        self.board_info.field_size_x = 0

    def get_filename(self):
        filename = 'Chess_'
        filename += self.get_kind_letter()
        filename += 'd' if self.color == 'B' else 't' + 't45.svg'
        return filename

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
    @staticmethod
    def get_kind_letter():
        return "k"

    def draw(self):
        self.draw_picture(self.get_filename())


class Queen(Piece):
    @staticmethod
    def get_kind_letter():
        return "q"

    def draw(self):
        self.draw_picture(self.get_filename())


class Bishop(Piece):
    @staticmethod
    def get_kind_letter():
        return "b"

    def draw(self):
        self.draw_picture(self.get_filename())


class Rook(Piece):
    @staticmethod
    def get_kind_letter():
        return "r"

    def draw(self):
        self.draw_picture(self.get_filename())


class Knight(Piece):
    @staticmethod
    def get_kind_letter():
        return "n"

    def draw(self):
        self.draw_picture(self.get_filename())


class Pawn(Piece):
    @staticmethod
    def get_kind_letter():
        return "p"

    def draw(self):
        self.draw_picture(self.get_filename())


if __name__ == '__main__':
    rook = Rook(1, 1, None, "W")
    print(rook.get_filename())
