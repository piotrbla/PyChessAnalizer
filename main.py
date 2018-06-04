from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from board import Board

SCREEN_HEIGHT_BORDER = 160
SCREEN_WIDTH_BORDER = 120


class BoardInfo:
    def __init__(self, field_size_x, field_size_y, start_x, start_y, painter):
        self.field_size_x = field_size_x
        self.field_size_y = field_size_y
        self.start_x = start_x
        self.start_y = start_y
        self.painter = painter



class MainGUI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen = QDesktopWidget().screenGeometry()
        self.screen_width = self.screen.width() - SCREEN_WIDTH_BORDER
        self.screen_height = self.screen.height() - SCREEN_HEIGHT_BORDER
        self.setGeometry(SCREEN_WIDTH_BORDER, SCREEN_HEIGHT_BORDER, self.screen_width, self.screen_height)
        self.setWindowTitle('Chess Analyzer')
        self.show()
        self.painter = QPainter()
        self.board_info = BoardInfo(0, 0, 2, 2, self.painter)
        self.center()

    def center(self):
        screen = self.screen
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def paintEvent(self, event):
        self.painter.begin(self)
        self.painter.setPen(Qt.darkGreen)
        self.draw_chessboard()
        self.draw_pieces()
        self.painter.end()

    def draw_chessboard(self):
        size = self.size()
        width_border = SCREEN_HEIGHT_BORDER
        height_border = SCREEN_HEIGHT_BORDER
        board_start_x = 2
        board_start_y = 2
        board_width = (size.width() - width_border) / 4 * 3
        board_height = size.height() - height_border

        x = board_start_x
        y = board_start_y
        x_diff = int((board_width - 2 * x) / 8)
        y_diff = int((board_height - 2 * y) / 8)
        board = Board()
        corn_silk_color = QColor(255, 248, 220)
        saddle_brown_color = QColor(139, 69, 19)
        antique_white_color = QColor(250, 235, 215)
        self.painter.fillRect(10, 10, 50, 50, corn_silk_color)
        self.painter.fillRect(110, 110, 50, 50, saddle_brown_color)
        self.painter.fillRect(x, y, board_width - x, board_height - y, corn_silk_color)
        for fields_row in reversed(board.fields):
            for field in fields_row:
                field_color = antique_white_color if (field.c + field.r) % 2 else saddle_brown_color
                self.painter.fillRect(x, y, x_diff, y_diff, field_color)
                x += x_diff
            y += y_diff
            x = board_start_x

    def draw_pieces(self):
        from pieces import Pawn
        pawn = Pawn(2, 1, self.board_info)
        for i in range(20):
            pawn.draw(None, 29*i, 19)
#           return [pawn]


def main():
    app = QApplication([])
    gui = MainGUI()
    app.exec_()


if __name__ == '__main__':
    main()
