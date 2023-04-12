# Задание 4.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку
# конструктора класса (метод init()), который должен принимать
# данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31 22
# 37 43
# 51 86
#
# 3 5 32
# 2 4 6
# -1 64 -8
#
# 3 5 8 3
# 8 3 7 1
#
# Следующий шаг — реализовать перегрузку метода str()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации
# операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым
# элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

new_matrix = Matrix([[3, 5, 32],
                    [2, 4, 6],
                    [-1, 64, 8]],
                   [[39, 6, 3],
                    [8, 2, 73],
                    [54, 5, 67]])

print(new_matrix.__add__())