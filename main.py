import tkinter as tk


class MainGUI:
    def __init__(self):
        root = tk.Tk()
        screen_width = str(root.winfo_screenwidth()-90)
        screen_height = str(root.winfo_screenheight()-320)
        root.geometry(screen_width + "x" + screen_height)
        self.root = root
        root.title("Chess Analyzer")
        main_menu = tk.Menu(root)
        root.config(menu=main_menu)
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label="Plik", menu=file_menu)
        file_menu.add_command(label="Nowy", command=self.callback)
        file_menu.add_command(label="Otworz", command=self.callback)
        file_menu.add_separator()
        file_menu.add_command(label="Wyjście", command=self.callback)

    def mainloop(self):
        self.root.mainloop()

    def callback(self):
        print("called the callback!")


def main():
    gui = MainGUI()
    gui.mainloop()


if __name__ == '__main__':
    main()
