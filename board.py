class Field:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.letter = chr(c + ord('A') - 1)


class Board:
    def __init__(self):
        self.fields = []
        for r in range(1, 9):
            fields_row = []
            for c in range(1, 9):
                fields_row.append(Field(r, c))
            self.fields.append(fields_row)

    def display(self):
        for fields_row in reversed(self.fields):
            for field in fields_row:
                print(field.letter, end='')
                print(field.r, end=' ')
            print()

    def display_reversed(self):
        for fields_row in self.fields:
            for field in reversed(fields_row):
                print(field.letter, end='')
                print(field.r, end=' ')
            print()

def main():
    b = Board()
    b.display()
    b.display_reversed()


if __name__ == '__main__':
    main()
