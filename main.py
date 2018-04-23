import tkinter as tk


class MainGUI:
    def __init__(self):
        root = tk.Tk()
        self.screen_width = root.winfo_screenwidth()-40
        self.screen_height = root.winfo_screenheight()-220
        root.geometry("{}x{}+10+10".format(self.screen_width, self.screen_height))
        self.root = root
        self.canvas = self.draw_chessboard()
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
        width_border = 250
        height_border = 130
        board_start_x = 2
        board_start_y = 2
        board_width = self.screen_width - width_border
        board_height = self.screen_height - height_border
        canvas = tk.Canvas(self.root, width=board_width, height=board_height)
        canvas.pack()
        canvas.create_rectangle(
            board_start_x, board_start_y, board_width - board_start_x, board_height - board_start_y, fill="cornsilk2")
        canvas.create_rectangle(2, 2, board_width - 2, board_height - 2, fill="saddle brown")
        canvas.create_rectangle(2, 2, board_width /2, board_height / 2, fill="antique white")
        return canvas

    def mainloop(self):
        self.root.mainloop()

    def callback(self):
        print("called the callback!")


def main():
    gui = MainGUI()
    gui.mainloop()


if __name__ == '__main__':
    main()
