class Matrix:
    def __init__(self, args):
        self.matrix = []
        self.matrix.append(args[0])
        index = 1
        while index < len(args):
            if type(args[index]) is list and len(args[index]) == len(args[0]):
                self.matrix.append(args[index])
            else:
                raise ValueError(f'All arguments should be lists and length of all list should be the same')
            index += 1

    def __str__(self):
        str_matrix = "|"
        for index_w in range(len(self.matrix)):
            for index_h in range(len(self.matrix[index_w])):
                space = ' '
                if index_h == (len(self.matrix[index_w]) - 1):
                    space = ''
                str_matrix += str(self.matrix[index_w][index_h]) + space
            new_line = "|\n|"
            if index_w == (len(self.matrix) - 1):
                new_line = "|\n"
            str_matrix += new_line
        return str_matrix

    def __add__(self, other):
        index = 0
        result = []
        while index < len(self.matrix):
            result.append([matrix_1 + matrix_1 for matrix_1, matrix_2 in zip(self.matrix[index], other.matrix[index])])
            index += 1
        # print(result)
        return result


a1 = Matrix([[1, 3, 4], [2, 4, 7]])
a2 = Matrix([[1, 3, 4], [2, 4, 7]])
print(a1)
print(Matrix(a1+a2))
