import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from board import Board

SCREEN_HEIGHT_BORDER = 160
SCREEN_WIDTH_BORDER = 420

# Back up the reference to the exception hook
sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


class BoardInfo:
    def __init__(self, start_x, start_y, field_size_x, field_size_y, painter, board_reversed=False):
        self.field_size_x = field_size_x
        self.field_size_y = field_size_y
        self.start_x = start_x
        self.start_y = start_y
        self.painter = painter
        self.board_reversed = board_reversed
        self.pieces = []
        self.set_pieces_on_starting_position()

    def get_position(self, c, r):
        if self.board_reversed:
            x = self.start_x + 7 * self.field_size_x - (c - 1) * self.field_size_x
            y = self.start_y + (r - 1) * self.field_size_y
        else:
            x = self.start_x + (c - 1) * self.field_size_x
            y = self.start_y + 7 * self.field_size_y - (r - 1) * self.field_size_y
        return x, y

    def get_mouse_position(self, x, y):
        if self.start_x > x or self.start_y > y:
            return 0, 0
        if self.start_x + 8 * self.field_size_x < x or \
                self.start_y + 8 * self.field_size_y < y:
            return 0, 0
        c = (x - self.start_x + self.field_size_x) // self.field_size_x
        r = (y - self.start_y + self.field_size_y) // self.field_size_y
        if self.board_reversed:
            c = 9 - c
        else:
            r = 9 - r
        return c, r

    def set_pieces_on_starting_position(self):
        from pieces import Pawn, King, Rook, Knight, Bishop, Queen
        for i in range(1, 9):
            self.pieces.append(Pawn(2, i, self, "W"))
            self.pieces.append(Pawn(7, i, self, "B"))

        self.pieces.append(Rook(1, 1, self, "W"))
        self.pieces.append(Knight(1, 2, self, "W"))
        self.pieces.append(Bishop(1, 3, self, "W"))
        self.pieces.append(Queen(1, 4, self, "W"))
        self.pieces.append(King(1, 5, self, "W"))
        self.pieces.append(Bishop(1, 6, self, "W"))
        self.pieces.append(Knight(1, 7, self, "W"))
        self.pieces.append(Rook(1, 8, self, "W"))
        self.pieces.append(Rook(8, 1, self, "B"))
        self.pieces.append(Knight(8, 2, self, "B"))
        self.pieces.append(Bishop(8, 3, self, "B"))
        self.pieces.append(Queen(8, 4, self, "B"))
        self.pieces.append(King(8, 5, self, "B"))
        self.pieces.append(Bishop(8, 6, self, "B"))
        self.pieces.append(Knight(8, 7, self, "B"))
        self.pieces.append(Rook(8, 8, self, "B"))

    def make_move(self, source_r, target_r, source_c, target_c):
        #print('S:', source_r, source_c)
        #print('T:', target_r, target_c)
        #return
        for piece in self.pieces:
            if piece.r == source_r and piece.c == source_c:
                if piece.check_rules(target_r, target_c):
                    piece.r = target_r  # TODO: move to method
                    piece.c = target_c
                else:
                    pass
                    # TODO: add info about impossible move (color field to red?)
                break


class MainGUI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clicked_r = 0
        self.clicked_c = 0
        self.screen = QDesktopWidget().screenGeometry()
        self.screen_width = self.screen.width() - SCREEN_WIDTH_BORDER
        self.screen_height = self.screen.height() - SCREEN_HEIGHT_BORDER
        self.setGeometry(SCREEN_WIDTH_BORDER, SCREEN_HEIGHT_BORDER, self.screen_width, self.screen_height)
        self.setWindowTitle('Chess Analyzer')
        self.show()
        self.painter = QPainter()
        self.board_info = BoardInfo(0, 0, 8, 8, self.painter)
        self.center()

    def center(self):
        screen = self.screen
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

    def paintEvent(self, event):
        self.painter.begin(self)
        self.draw_chessboard()
        self.draw_pieces()
        self.painter.end()

    def mousePressEvent(self, event: QMouseEvent):
        x = event.x()
        y = event.y()
        c, r = self.board_info.get_mouse_position(x, y)
        print(x, y, "r:", r, "c:", c)

        if self.clicked_r > 0 and self.clicked_c > 0:  # TODO: check if any piece is clicked
            self.board_info.make_move(self.clicked_r, r, self.clicked_c, c)
        self.clicked_r = r
        self.clicked_c = c

        event.ignore()
        self.repaint()

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
        self.board_info = BoardInfo(board_start_x, board_start_y, x_diff, y_diff, self.painter)
        board = Board()
        corn_silk_color = QColor(255, 248, 220)
        saddle_brown_color = QColor(139, 69, 19)
        antique_white_color = QColor(250, 235, 215)
        saddle_brown_color_checked = QColor(99, 39, 9)
        antique_white_color_checked = QColor(200, 195, 185)
        self.painter.fillRect(10, 10, 50, 50, corn_silk_color)
        self.painter.fillRect(110, 110, 50, 50, saddle_brown_color)
        self.painter.fillRect(x, y, int(board_width - x), int(board_height - y), corn_silk_color)

        for fields_row in reversed(board.fields):
            for field in fields_row:
                field_color = antique_white_color if (field.c + field.r) % 2 else saddle_brown_color

                if self.board_info.board_reversed:
                    if self.clicked_r == 9 - field.r and self.clicked_c == 9 - field.c:
                        field_color = antique_white_color_checked \
                            if (field.c + field.r) % 2 \
                            else saddle_brown_color_checked
                else:
                    if self.clicked_r == field.r and self.clicked_c == field.c:
                        field_color = antique_white_color_checked \
                            if (field.c + field.r) % 2 \
                            else saddle_brown_color_checked
                self.painter.fillRect(x, y, x_diff, y_diff, field_color)
                x += x_diff
            y += y_diff
            x = board_start_x

    def draw_pieces(self):
        for piece in self.board_info.pieces:
            piece.draw()


# noinspection PyBroadException
def main():
    app = QApplication([])
    gui = MainGUI()
    # app.exec_()
    try:
        sys.exit(app.exec_())
    except Exception as ex:
        print("Exiting: ", ex)


if __name__ == '__main__':
    main()
