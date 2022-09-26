class Step(object):

    def __init__(self, st_number=1, end_number=10):
        self.max = end_number + 1
        self.number = st_number - 1

    def step(self):
        self.number += 1
        if self.number >= self.max:
            self.number = 1
        return self.number


class Sudoku(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.index_list = self.__get_index()
        self.first_index_list = []

    def check(self):
        pass

    def get_result(self):
        out = self.__check()
        if out is False:
            print('不是正确的数独')
            return self.matrix, False
        result, index = self.try_values(0)
        while result is not True:
            result, index = self.try_values(index - 1)
        return self.matrix, True

    def try_values(self, start_index):
        for index, values in enumerate(self.index_list):
            if index < start_index:
                continue
            s = Step()
            num = s.step()
            index_line = values[0]
            index_row = values[1]
            value_list = values[2]
            lines = self.get_lines(index_line)
            rows = self.get_rows(index_row)
            matrix = self.get_matrix(index_line, index_row)
            while num in lines or num in rows or num in matrix or num in value_list:
                num = s.step()
            if num == 10:
                last_values = self.index_list[index - 1]
                last_line = last_values[0]
                last_row = last_values[1]
                self.matrix[last_line][last_row] = 0
                self.reset(start_index=index - 1)
                return False, index
            self.matrix[index_line][index_row] = num
            if num in value_list:
                continue
            value_list.append(num)
            self.index_list[index][2] = value_list

        return True, 0

    def reset(self, start_index):
        for index, values in enumerate(self.index_list):
            if index > start_index:
                last_values = self.index_list[index - 1]
                last_line = last_values[0]
                last_row = last_values[1]
                self.matrix[last_line][last_row] = 0
                self.index_list[index][2] = []

    def get_lines(self, line):
        l = []
        lines = self.matrix[line]
        for i in lines:
            l.append(i)
        return l

    def get_rows(self, row):
        rows = []
        for i in self.matrix:
            rows.append(i[row])
        return rows

    def get_matrix(self, line, row):
        m = []
        for index_1, i in enumerate(self.matrix):
            for index_2, j in enumerate(i):
                a = index_1 // 3
                b = index_2 // 3
                c = line // 3
                d = row // 3
                if a == c and b == d:
                    m.append(j)
        return m

    def __get_index(self):
        index_list = []
        for index_line, lines in enumerate(self.matrix):
            for index_row, value in enumerate(lines):
                if value == 0:
                    index_ = [index_line, index_row, []]
                    index_list.append(index_)
        return index_list

    def __check(self):
        for i in range(9):
            lines = self.get_lines(i)
            rows = self.get_rows(i)
            if len(lines) != 9 or len(rows) != 9:
                return False
            line_list = []
            row_list = []
            for j in lines:
                if j in line_list:
                    return False
                if j != 0:
                    line_list.append(j)
            for j in rows:
                if j in row_list:
                    return False
                if j != 0:
                    row_list.append(j)
        for i in range(9):
            for j in range(9):
                if i // 3 == 0 and j // 3 == 0:
                    matrixs = self.get_matrix(i, j)
                    if len(matrixs) != 9:
                        return False
                    matrixs_list = []
                    for k in matrixs:
                        if k in matrixs_list:
                            return False
                        if k != 0:
                            matrixs_list.append(k)
        return True


if __name__ == '__main__':
    from sudoku_example import *
    import time

    sudo = Sudoku(example4)
    # print(d.get_matrix(8,8))
    t1 = time.time()
    print(sudo.get_result())
    t2 = time.time()
    print(t2 - t1)
