import tkinter as tk


class MainGUI:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.title("Chess Analyzer")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = tk.IntVar()
        self.total_label_text.set(self.total)
        self.total_label = tk.Label(root, textvariable=self.total_label_text)

        self.label = tk.Label(root, text="Total:")

        validation_cmd = root.register(self.validate)  # we have to wrap the command
        self.entry = tk.Entry(root, validate="key", validatecommand=(validation_cmd, '%P'))

        self.add_button = tk.Button(root, text="+", command=lambda: self.update("add"))
        self.subtract_button = tk.Button(root, text="-", command=lambda: self.update("subtract"))
        self.reset_button = tk.Button(root, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=tk.W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=tk.E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=tk.W + tk.E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=tk.W + tk.E)

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else:  # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, tk.END)


def callback():
    print("called the callback!")


def create_window():
    gui = MainGUI()
    gui.mainloop()
    # root = tk.Tk()
    # main_menu = tk.Menu(root)
    # root.config(menu=main_menu)
    # file_menu = tk.Menu(main_menu)
    #
    # main_menu.add_cascade(label="Plik", menu=file_menu)
    # file_menu.add_command(label="Nowy", command=callback)
    # file_menu.add_command(label="Otworz", command=callback)
    # file_menu.add_separator()
    # file_menu.add_command(label="Wyjście", command=callback)



def main():
    create_window()


if __name__ == '__main__':
    main()
