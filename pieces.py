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
        filename = 'Chess_' + self.get_kind_letter()
        filename += 'd' if self.color == 'B' else 'l'
        filename += 't45.svg'
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
    board = None
    pieces = []
    for i in range(1, 9):
        pieces.append(Pawn(2, i, board, "W"))
        pieces.append(Pawn(7, i, board, "B"))

    pieces.append(Rook(1, 1, board, "W"))
    pieces.append(Knight(1, 2, board, "W"))
    pieces.append(Bishop(1, 3, board, "W"))
    pieces.append(Queen(1, 4, board, "W"))
    pieces.append(King(1, 5, board, "W"))
    pieces.append(Bishop(1, 6, board, "W"))
    pieces.append(Knight(1, 7, board, "W"))
    pieces.append(Rook(1, 8, board, "W"))
    pieces.append(Rook(8, 1, board, "B"))
    pieces.append(Knight(8, 2, board, "B"))
    pieces.append(Bishop(8, 3, board, "B"))
    pieces.append(Queen(8, 4, board, "B"))
    pieces.append(King(8, 5, board, "B"))
    pieces.append(Bishop(8, 6, board, "B"))
    pieces.append(Knight(8, 7, board, "B"))
    pieces.append(Rook(8, 8, board, "B"))
    for piece in pieces:
        print(piece.get_filename())
