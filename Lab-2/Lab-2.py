import numpy as np
import matplotlib as mpl
import random as ran
'''Формируется матрица F следующим образом: 
1.1 скопировать в нее A 
1.2 если количество нулей в B больше, чем в E, то поменять в ней местами B и C симметрично, 
1.3 иначе B и E поменять местами несимметрично. 
При этом матрица A не меняется. 
После чего 
2.1 если определитель матрицы A больше суммы диагональных элементов матрицы F 
2.2 то вычисляется выражение: A*AT - K * F 
2.3 иначе вычисляется выражение (A-1 +G-F-1)*K, где G-нижняя треугольная матрица, полученная из A. 
3 Выводятся по мере формирования A, F и все матричные операции последовательно. '''
def create_submatrixes_random(s):
    matrixB = np.random.randint(-10,10,size=(s,s))
    matrixC = np.random.randint(-10,10,size=(s,s))
    matrixD = np.random.randint(-10,10,size=(s,s))
    matrixE = np.random.randint(-10,10,size=(s,s))
    return matrixB,matrixC,matrixD,matrixE

def create_submatrixes_txt():
    None

def create_submatrixes_gen():
    None


def create_matrix_from_sub(b,c,d,e):
    m1 = np.concatenate((b,e),axis=1)
    m2 = np.concatenate((c,d), axis=1)
    mA = np.concatenate((m1,m2), axis=0)
    return mA

def search_zeros(sub):
    return len(sub[sub == 0])

def create_matrixF(result,b,c,d,e):
    if result == 1:
        m1 = np.concatenate((c,e),axis=1)
        m2 = np.concatenate((b,d),axis=1)
        mF = np.concatenate((m1,m2),axis=0)
        return mF
    else:
        invert_b = np.flip(b)
        sort_e = np.sort(e)
        m1 = np.concatenate((sort_e,invert_b),axis=1)
        m2 = np.concatenate((c,d),axis=1)
        mF = np.concatenate((m1,m2),axis=0)
        return mF
    
def low_triag_matrix():
    None

def matrix_expression():
    None
#----Main---

while True:
    chooser = int(input("Как создаём матрицу:\n1 - Рандомом\n2 - из файла\n3 - генератором\nВаш выбор: "))
    if chooser == 1:
        size = int(input("Введите размер матрицы: "))
        submatrixB,submatrixC,submatrixD,submatrixE = create_submatrixes_random(size)
        matrixA = create_matrix_from_sub(submatrixB,submatrixC,submatrixD,submatrixE)
        break
    else: 
        print("In dev")

print("Результат")
print(f"Подматрица B:\n{submatrixB}\nПодматрица C:\n{submatrixC}\nПодматрица D:\n{submatrixD}\nПодматрица E:\n{submatrixE}")
print(f"Матрица А:\n{matrixA}")
print(f"Количество нулей в B: {search_zeros(submatrixB)}")
print(f"Количество нулей в E: {search_zeros(submatrixE)}")
result = 1 if search_zeros(submatrixB) > search_zeros(submatrixE) else 0
matrixF = create_matrixF(result,submatrixB,submatrixC,submatrixD,submatrixE)
print(f"Матрица F:\n{matrixF}")
det_matrix_A = np.linalg.det(matrixA)
print(f"Определитель матрицы А: {det_matrix_A}")
diag_sum = sum(np.diagonal(matrixF)) + sum(np.fliplr(matrixF).diagonal())
print(f"Сумма диагоналей матрицы F: {diag_sum}")
result = 1 if det_matrix_A > diag_sum else 0