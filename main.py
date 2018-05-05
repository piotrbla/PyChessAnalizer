import tkinter as tk
from board import Board


class BoardInfo:
    def __init__(self, field_size_x, field_size_y, start_x, start_y):
        self.field_size_x = field_size_x
        self.field_size_y = field_size_y
        self.start_x = start_x
        self.start_y = start_y


class MainGUI:
    def __init__(self):
        # TODO: change GUI to pygame/arcade
        root = tk.Tk()
        self.screen_width = root.winfo_screenwidth() - 40
        self.screen_height = root.winfo_screenheight() - 220
        root.geometry("{}x{}+10+10".format(self.screen_width, self.screen_height))
        self.root = root
        self.canvas_frame = tk.Frame(root, width=self.screen_width / 1.3, height=self.screen_height)
        self.canvas_frame.pack(side=tk.LEFT)
        self.right_frame = tk.Frame(root)
        self.right_frame.configure(borderwidth=15, background='green')
        self.right_frame.pack()
        self.run_button = tk.Button(self.right_frame, text="Uruchom", command=self.callback)
        self.run_button.pack()
        self.sec_button = tk.Button(self.right_frame, text="Uruchom", command=self.callback)
        self.sec_button.pack()
        self.board_info = BoardInfo(0, 0, 2, 2)
        self.canvas = self.draw_chessboard()
        self.pieces = self.draw_pieces()

        root.title("Chess Analyzer")
        main_menu = tk.Menu(root)
        root.config(menu=main_menu)
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label="Plik", menu=file_menu)
        file_menu.add_command(label="Nowy", command=self.callback)
        file_menu.add_command(label="Otworz", command=self.callback)
        file_menu.add_separator()
        file_menu.add_command(label="Wyjście", command=self.root.quit)

    def draw_chessboard(self):
        width_border = 550
        height_border = 130
        board_width = self.screen_width - width_border
        board_height = self.screen_height - height_border
        canvas = tk.Canvas(self.canvas_frame, width=board_width, height=board_height)
        canvas.pack()
        x = self.board_info.start_x
        y = self.board_info.start_y
        x_diff = self.board_info.field_size_x = (board_width - 2 * x) / 8
        y_diff = self.board_info.field_size_y = (board_height - 2 * y) / 8
        self
        board = Board()
        canvas.create_rectangle(x, y, board_width - x, board_height - y, fill="cornsilk2")
        for fields_row in reversed(board.fields):
            for field in fields_row:
                field_color = "antique white" if (field.c + field.r) % 2 else "saddle brown"
                canvas.create_rectangle(x, y, x + x_diff, y + y_diff, fill=field_color)
                x += x_diff
            y += y_diff
            x = self.board_info.start_x
        return canvas

    def mainloop(self):
        self.root.mainloop()

    def callback(self):
        print("called the callback!")

    def draw_pieces(self):
        from pieces import Pawn
        pawn = Pawn(2, 1, self.board_info)
        for i in range(10):
            pawn.draw(self.canvas, 29*i, 19)
        return [pawn]


def main():
    gui = MainGUI()
    gui.mainloop()


if __name__ == '__main__':
    main()
