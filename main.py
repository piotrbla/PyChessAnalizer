from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random
#import tkinter as tk
from board import Board


class MainGUI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = "Piotr Błaszyński\n Zażółć gęślą jaźń \n"
        self.setGeometry(900, 300, 880, 370)
        self.setWindowTitle('Chess Analyzer')
        self.show()
        self.painter = QPainter()

    def paintEvent(self, event):
        self.painter.begin(self)
        self.draw_decorative_text(event, self.painter)
        self.painter.setPen(Qt.darkGreen)
        self.draw_chessboard()

        # pawn_image = QPixmap("./Chess_plt45.png")
        # self.painter.drawPixmap(100, 10, 50, 50, pawn_image)
        self.painter.end()

    def draw_decorative_text(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 14))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

    # def __init__(self):
    #     root = tk.Tk()
    #     self.screen_width = root.winfo_screenwidth() - 40
    #     self.screen_height = root.winfo_screenheight() - 220
    #     root.geometry("{}x{}+10+10".format(self.screen_width, self.screen_height))
    #     self.root = root
    #     self.canvas_frame = tk.Frame(root, width=self.screen_width / 1.3, height=self.screen_height)
    #     self.canvas_frame.pack(side=tk.LEFT)
    #     self.right_frame = tk.Frame(root)
    #     self.right_frame.configure(borderwidth=15, background='green')
    #     self.right_frame.pack()
    #     self.run_button = tk.Button(self.right_frame, text="Uruchom", command=self.callback)
    #     self.run_button.pack()
    #     self.sec_button = tk.Button(self.right_frame, text="Uruchom", command=self.callback)
    #     self.sec_button.pack()
    #     self.canvas = self.draw_chessboard()
    #
    #     main_menu = tk.Menu(root)
    #     root.config(menu=main_menu)
    #     file_menu = tk.Menu(main_menu)
    #     main_menu.add_cascade(label="Plik", menu=file_menu)
    #     file_menu.add_command(label="Nowy", command=self.callback)
    #     file_menu.add_command(label="Otworz", command=self.callback)
    #     file_menu.add_separator()
    #     file_menu.add_command(label="Wyjście", command=self.root.quit)

    def draw_chessboard(self):
        size = self.size()

        # for i in range(10000):
        #     x = random.randint(1, size.width() - 1)
        #     y = random.randint(1, size.height() - 1)
        #     self.painter.drawPoint(x, y)

        width_border = 550
        height_border = 130
        board_start_x = 2
        board_start_y = 2
        board_width = size.width() - width_border
        board_height = size.height() - height_border
        # canvas = tk.Canvas(self.canvas_frame, width=board_width, height=board_height)
        # canvas.pack()
        x = board_start_x
        y = board_start_y
        x_diff = (board_width - 2 * x) / 8
        y_diff = (board_height - 2 * y) / 8
        board = Board()
        self.painter.FillRect(x, y, board_width - x, board_height - y, darkRed) # fill="cornsilk2")
        # for fields_row in reversed(board.fields):
        #     for field in fields_row:
        #         field_color = "antique white" if (field.c + field.r) % 2 else "saddle brown"
        #         self.painter.drawRect(x, y, x + x_diff, y + y_diff, fill=field_color)
        #         x += x_diff
        #     y += y_diff
        #     x = board_start_x

    def mainloop(self):
        self.root.mainloop()

    def callback(self):
        print("called the callback!")


def main():
    app = QApplication([])
    gui = MainGUI()
    app.exec_()


if __name__ == '__main__':
    main()
