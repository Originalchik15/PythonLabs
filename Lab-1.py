import random as ran

def matrix_create_from_txt():
    size = 0
    matrix = []
    with open("matrix.txt", "r") as f:
        for line in f:
            row = list(map(int, line.split(',')))
            matrix.append(row)
            size += 1
    return matrix,size

def matrix_create_random(size):
    return [[ran.randint(-10, 10) for i in range(size)] for j in range(size)]

def area_part_counter(matrix, size, area_num, count_elements=False):
    area = []
    count_pos = 0
    count_neg = 0

    for i in range(size):
        for j in range(size):
            if in_area(i, j, size, area_num):
                area.append(matrix[i][j])
                if count_elements:
                    if area_num == 2 and j % 2 == 0 and matrix[i][j] >= 0:
                        count_pos += 1
                    if area_num == 4 and j % 2 != 0 and matrix[i][j] < 0:
                        count_neg += 1
    if count_elements:
        return area, count_pos if area_num == 2 else count_neg
    return area


def in_area(i, j, size, area_num):
    if area_num == 2: 
        return i < j and i + j < size - 1
    elif area_num == 3:  
        return i < j and i + j > size - 1
    elif area_num == 4:  
        return i > j and i + j > size - 1
    return False

def area_replace(matrix, size, result, part2, part3, part4):
    if result > 0:  
        replace_area(matrix, size, part4, 3)
        replace_area(matrix, size, part3, 4)
    else:  
        part2 = list(reversed(part2))
        part3 = sorted(part3)
        replace_area(matrix, size, part3, 2)
        replace_area(matrix, size, part2, 3)
    return matrix

def replace_area(matrix, size, new_values, area_num):
    idx = 0
    for i in range(size):
        for j in range(size):
            if in_area(i, j, size, area_num):
                matrix[i][j] = new_values[idx]
                idx += 1

def matrix_sum(m1, m2, size):
    return [[m1[i][j] + m2[i][j] for j in range(size)] for i in range(size)]

def matrix_transpose(matrix, size):
    return [[matrix[j][i] for j in range(size)] for i in range(size)]

def matrix_multiply_by_k(matrix, size, k):
    return [[matrix[i][j] * k for j in range(size)] for i in range(size)]

def matrix_multiply_by_matrix(m1, m2, size):
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def matrix_subtract(m1, m2, size):
    return [[m1[i][j] - m2[i][j] for j in range(size)] for i in range(size)]

def matrix_copy(matrix, size):
    return [[matrix[i][j] for j in range(size)] for i in range(size)]

def matrix_print(matrix, size):
    for row in matrix:
        print(row)
    print()

matrix_check = False
while True:
    try:
        k = int(input("|----Введите число K: "))
        break
    except:
        print("Ошибка при вводе числа К")
    
while not matrix_check:
    try:
        print("|----Как создаём матрицу--------------|\n|----1. Из .txt ---------------|\n|----2. Рандомом ---------------------|")
        choose = int(input("|----Ваш выбор: "))
        if choose == 1:
            matrixA,size = matrix_create_from_txt()
            matrix_check = True
        elif choose == 2:
            size = int(input("|----Введите размер матрицы (>= 3): "))
            matrixA = matrix_create_random(size)
            matrix_check = True
        else:
            print("|----Неверный выбор")
    except:
        print("Ошибка при создании матрицы")

matrixF = matrix_copy(matrixA, size)
print("|----Ваша матрица(А): ")
matrix_print(matrixF, size)

print("|----Создаём матрицу(F)")
p2, positive = area_part_counter(matrixF, size, 2, count_elements=True)
p3 = area_part_counter(matrixF, size, 3)
p4, negative = area_part_counter(matrixF, size, 4, count_elements=True)

matrixF = area_replace(matrixF, size, positive - negative, p2, p3, p4)
print("|----Матрица(F) создана: ")
matrix_print(matrixF, size)

matsum = matrix_sum(matrixF, matrixA, size)
print("|----(F+A)----|")
matrix_print(matsum, size)

mattranspose = matrix_transpose(matrixA, size)
print("|----At----|")
matrix_print(mattranspose, size)

matmulty = matrix_multiply_by_k(matrixF, size, k)
print("|----F*k----|")
matrix_print(matmulty, size)

matmultymat = matrix_multiply_by_matrix(matsum, mattranspose, size)
print("|----(F+A) * At----|")
matrix_print(matmultymat, size)

answer = matrix_subtract(matmultymat, matmulty, size)
print("|----(F+A)*At - K*F =")
matrix_print(answer, size)



