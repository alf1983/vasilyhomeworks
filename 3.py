class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return self.cell_count + other.cell_count

    def __sub__(self, other):
        result = self.cell_count - other.cell_count
        if result < 0:
            return "Вычитение невозможно"
        return result

    def __mul__(self, other):
        return self.cell_count * other.cell_count

    def __floordiv__(self, other):
        return self.cell_count // other.cell_count

    def make_order(self, row_size):
        result = ""
        row = 0
        for cell in range(self.cell_count):
            result += "*"
            row += 1
            if row == row_size:
                row = 0
                result += "\n"
        return result


cell_1 = Cell(14)
cell_2 = Cell(17)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_2 // cell_1)
print(cell_2.make_order(5))
