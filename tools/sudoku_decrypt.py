# -*- coding: utf-8 -*-
"""数独解密程序"""


# 计数器
class Step(object):
    def __init__(self, st_number=1, end_number=10):
        self.max = end_number + 1
        self.number = st_number - 1

    def step(self):
        self.number += 1
        if self.number >= self.max:
            self.number = 1
        return self.number


# 数独解密
class Sudoku(object):
    def __init__(self, matrix):
        self.in_matrix = matrix
        self.matrix = matrix
        self.index_list = self.__get_index()  # 获取待解密的数值列表[raw,line,[values]]

    def get_result(self):
        out = self.__check()  # 初步检查数独是否符合要求
        if out is False:
            print("不是正确的数独！")
            return self.in_matrix, False
        result, index = self.__try_values(0)
        while result is not True:  # 如果尝试失败，再尝试上一个值
            result, index = self.__try_values(index - 1)
            if result is False and index == 0:  # 如果第一个值都尝试完但是还没解出来，表示无解
                print("此数独无解！")
                return self.in_matrix, False

        return self.matrix, True

    def __try_values(self, start_index):
        for index, values in enumerate(self.index_list):
            if index < start_index:
                continue
            s = Step()
            num = s.step()
            index_line = values[0]  # 待定值的行索引
            index_row = values[1]   # 待定值的列索引
            value_list = values[2]      # 尝试过的值
            lines = self.__get_lines(index_line)   # 此行已存在的值
            rows = self.__get_rows(index_row)   # 此列已存在的值
            matrix = self.__get_matrix(index_line, index_row)    # 此3x3方格已存在的值
            while num in lines or num in rows or num in matrix or num in value_list:
                num = s.step()          # 生成可填入数值
            if num == 10:   # 所有值都尝试过
                last_values = self.index_list[index - 1]  # 得到前一个待定值的信息
                last_line = last_values[0]
                last_row = last_values[1]
                self.matrix[last_line][last_row] = 0  # 重置前一个待定值
                self.__reset(start_index=index - 1)  # 回退
                return False, index   # 尝试失败
            self.matrix[index_line][index_row] = num   # 填入待定值
            if num in value_list:
                continue
            value_list.append(num)  # 更新尝试过的值
            self.index_list[index][2] = value_list  # 更新待定值列表

        return True, 0

    # 回退函数,重置尝试值后面所有待定值
    def __reset(self, start_index):
        for index, values in enumerate(self.index_list):
            if index > start_index:
                last_values = self.index_list[index - 1]
                last_line = last_values[0]
                last_row = last_values[1]
                self.matrix[last_line][last_row] = 0
                self.index_list[index][2] = []

    def __get_lines(self, line):
        l = []
        lines = self.matrix[line]
        for i in lines:
            l.append(i)
        return l

    def __get_rows(self, row):
        rows = []
        for i in self.matrix:
            rows.append(i[row])
        return rows

    def __get_matrix(self, line, row):
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

    # 获取待解密的数独列表
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
            lines = self.__get_lines(i)
            rows = self.__get_rows(i)
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
                    matrixs = self.__get_matrix(i, j)
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
    from unites import example_transform
    example = example_transform(example1)
    # print(example)
    print("输入:")
    for i in example:
        print(i)
    sudo = Sudoku(example)
    # print(d.get_matrix(8,8))
    t1 = time.time()
    out, res = sudo.get_result()
    if res:
        print("输出")
        for i in out:
            print(i)
    t2 = time.time()
    print("耗时:%.4f秒" %(t2 - t1))
