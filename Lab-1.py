import random as ran
#если 
#количество положительных элементов в четных столбцах в области 2 больше, чем 
#количество отрицательных  элементов в нечетных столбцах в области 4, то поменять в ней 
#симметрично области 3 и 4 местами, иначе  поменять местами области 2 и 3 местами 
#несимметрично. 
def menu_create_chooser():
     print("|----Как создаём матрицу--------------|\n|----1. Самостоятельно ---------------|\n|----2. Рандомом ---------------------|\n|----3. От одного числа до другого ---|")

def matrix_create_by_yourself(size): #Заполнение самостоятельно
    print("Создаём матрицу: ")
    
    matrix = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            while True:
                n = int(input("Строка "+str(i+1)+", столбец "+str(j+1)+": "))
                if n >= -10 or n <= 10:
                    break
                else:
                    print("Число должно быть от -10 до 10")
            matrix[i][j] = n

    return matrix

def matrix_create_random(size): # Заполнение рандомом потом
    matrix = [[ran.randint(-10,10) for i in range(size)] for j in range(size)]
    return matrix

def matrix_create_from_to(size,first,last): #Заполнение от одного числа до другого
    print("Создаём матрицу: ")
    start = first
    matrix = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = first
            first += 1
            if(first > last):
                first = start
    return matrix

def even_nums_check():#чётные
    a = 0

def odd_nums_check(): #нечётные
    a = 0
        
# def area_make(matrix, size): #Выделить диагонали
#     pl = 0
#     mi = 0
#     for i in range(size):
#         matrix[i][0 + pl] = "E"
#         matrix[i][-1 - mi] = "E"
#         pl += 1
#         mi += 1
#         print(matrix[i])
#     return matrix

def area_part_counter(matrix, size, area_num, for_count):
    first_area, second_area, third_area, fourth_area = [],[],[],[]
    for_second_count = 0
    for_fourth_count = 0
    if area_num == 1: # 1 Часть матрицы
        for i in range(size):
            for j in range(i):  
                if j < size - i - 1:  
                    first_area.append(matrix[i][j])
        return first_area
    elif area_num == 2: # --- 2 Часть матрицы
        for i in range(size):
            for j in range(i + 1, size):
                if j < size - i - 1:
                    second_area.append(matrix[i][j])
                    if j % 2 == 0 and matrix[i][j] >= 0 and for_count == 1:
                        for_second_count += 1
        return second_area, for_second_count if for_count == 1 else second_area

    elif area_num == 3: # 3 Часть матрицы
        for i in range(size):
            for j in range(i + 1, size):  
                if j > size - i - 1:  
                    third_area.append(matrix[i][j])
        return third_area
    elif area_num == 4: # --- 4 Часть матрицы
        for i in range(size):
            for j in range(i):
                if j > size - i - 1:
                    fourth_area.append(matrix[i][j])
                    if j % 2 != 1 and matrix[i][j] >= 0 and for_count == 1:
                        for_fourth_count += 1
        return fourth_area, for_fourth_count if for_count == 1 else fourth_area
                     
def area_replace(matrix,size,result,part2,part3,part4):
    if result > 0: #Симметрично 3 4
        k = 0
        for i in range(size): # -- 3я
            for j in range(i + 1, size):  
                if j > size - i - 1: 
                    matrix[i][j] = part4[k] #Здесь !!!!!!!!!!!
                    k += 1
        k = 0
        for i in range(size): # -- 4я
            for j in range(i): 
                if j > size - i - 1:
                    matrix[i][j] = part3[k]
                    k += 1
        return matrix

    elif result <= 0: #Несимметрично 2 3
        part2 = list(reversed(part2))
        part3 = list(sorted(part3))
        k = 0
        for i in range(size): # -- 2я
            for j in range(i + 1, size):
                if j < size - i - 1:
                    matrix[i][j] = part3[k]
        k = 0
        for i in range(size): # -- 3я
            for j in range(i + 1, size):  
                if j > size - i - 1:  
                    matrix[i][j] = part2[k]
        return matrix

def matrix_sum(m1,m2,size): #Сумма матриц
    for i in range(size): 
        for j in range(size):
            m1[i][j] += m2[i][j]
    return m1       

def matrix_transpose(matrix,size): #Транспонирование матрицы
    Tmatrix = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            Tmatrix[j][i] = matrix[i][j]
    return Tmatrix

def matrix_print(matrix,size):
    for i in range(size):
        print(matrix[i])
    return

def matrix_multiply_by_k(matrix,size,k):
    for i in range(size):
        for j in range(size):
            matrix[i][j] *= k
    return matrix

def matrix_multyply_by_matrix(m1, m2, size):
    # Стандартное умножение матриц
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += m1[i][k] * m2[k][j]  # Умножение строк и столбцов
    return result

def matrix_substract(m1,m2,size):
    for i in range(size):
        for j in range(size):
            m1[i][j] -= m2[i][j]
    return m1
def matrix_copy(matrix,size):
    copy = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            copy[i][j] += matrix[i][j]
    return copy
#-------------DEV-----------------
"""size = 4
matrix = matrix_create_from_to(size,-3,9)
print(matrix)
print("Первая часть: ",area_part_counter(matrix,size,1,0))
fi_part = area_part_counter(matrix,size,1,0)
print("Вторая часть: ",area_part_counter(matrix,size,2,1))
se_part, num1 = area_part_counter(matrix,size,2,1)
print("Третья часть: ",area_part_counter(matrix,size,3,0))
th_part = area_part_counter(matrix,size,3,0)
print("Четвёртая часть: ",area_part_counter(matrix,size,4,1))
fo_part, num2 = area_part_counter(matrix,size,4,1) 
area_replace(matrix,size,-9,se_part,th_part,fo_part)
Tmat = matrix_transpose(matrix,size)"""

#-------------------Main---------------
matrix_check = False
while True:
    try:
        k = int(input("|----Введите число которое нужно будет для примера: "))
        break
    except:
        print("Ошибка при вводе числа К")
while True:
    
    if matrix_check == False:
        try:
            menu_create_chooser() #Менюшка
            choose = int(input("|----Ваш выбор: "))
            if choose == 1: #Заполнение самостоятельно
                while True:
                    size = int(input("|----Введите размер матрицы (больше\равно 3): "))
                    if size >= 3: break  
                    else: print("|----Число должно быть больше либо равно 3")
                matrixA = matrix_create_by_yourself(size)
                matrix_check = True
            elif choose == 2:
                while True:
                    size = int(input("|----Введите размер матрицы (больше\равно 3): "))
                    if size >= 3: break  
                    else: print("|----Число должно быть больше либо равно 3")
                matrixA = matrix_create_random(size)
                matrix_check = True
            elif choose == 3: #Заполнение от одного числа до другого
                size = int(input("|----Введите размер матрицы (больше\равно 3): "))
                while True:
                    first = int(input("|----Введите число начала: "))
                    last = int(input("|----Введите число конца: "))
                    if first < last: break
                    else: print("|----Число начала должно быть меньше либо равно числу конца") 
                matrixA = matrix_create_from_to(size,first,last)
                matrix_check = True
            else: 
                print("|----Неверный выбор")
        except:
            print("|----Ошибка при создании матрицы")
    else:
        # matrixF = [[0 for i in range(size)] for j in range(size)]
        matrixF = matrix_copy(matrixA,size)
        print("|----Ваша матрица(А): ")
        matrix_print(matrixF,size)
        print("|----Создаём матрицу(F)")
        p1 = area_part_counter(matrixF,size,1,0)
        p2, positive = area_part_counter(matrixF,size,2,1)
        p3 = area_part_counter(matrixF,size,3,0)
        p4, negative = area_part_counter(matrixF,size,4,1)
        print("|----Матрица поделена на 4 части")
        while True:
            try:
                choose = int(input("|----Показать? (1 - да, 2 - нет): "))
                break
            except:
                print("Ошибка выбора ответа")
        if choose == 1:
            print("|----Первая часть: ",p1)
            print("|----Вторая часть: ",p2)
            print("|----Третья часть: ",p3)
            print("|----Четвёртая часть: ",p4)
            print("|----положительные элементы в четных столбцах области 2: ", positive)
            print("|----отрицательные элементы в нечетных столбцах области 4: ", negative)
        matrixF = area_replace(matrixF,size,positive-negative,p2,p3,p4)
        print("|----Матрица(F) создана: ")
        matrix_print(matrixF,size)
        print("|----Решаем следующий пример: (F+A)*At - K*F")
        # --- Сложение матриц ---
        matsum = matrix_sum(matrixF,matrixA,size)
        print("|----(F+A)----|")
        matrix_print(matsum,size)
        # --- Транспонирование матрицы ---
        mattranspose = matrix_transpose(matrixA,size)
        print("|----At----|")
        matrix_print(mattranspose,size)
        # --- Умножение на число ---
        matmulty = matrix_multiply_by_k(matrixF,size,k)
        print("|----F*k----|")
        matrix_print(matmulty,size)
        # --- Умножение на матрицу ---
        matmultymat = matrix_multyply_by_matrix(matsum,mattranspose,size)
        print("|----(F+A) * At----|")
        matrix_print(matmulty,size)
        # --- Вычитание ---
        answer = matrix_substract(matmultymat,matmulty,size)
        print("|----(F+A)*At - K*F =")
        matrix_print(answer,size)
        break