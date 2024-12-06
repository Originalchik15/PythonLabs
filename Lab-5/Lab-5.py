import math
import timeit

"""Задана рекуррентная функция. 
Область определения функции – натуральные числа. 
Написать программу сравнительного вычисления данной функции 
рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода. 
Результаты сравнительного исследования времени вычисления 
представить в табличной форме. 
Обязательное требование – минимизация времени выполнения и объема памяти.
F(x<2) = 1; F(n) = (-1)n*(2F(n-1)/n! + F(n-3)/(2n)!)"""

memo = {}
def fac(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    result = n * fac(n - 1)
    memo[n] = result
    return result

def F_rec(n):
    if n < 0:
        return 0
    if n < 2:
        return 1
    sign = -1 if n % 2 else 1
    pr = sign * (2 * F_rec(n-1) / fac(n) + F_rec(n-3) / fac(2*n))
    return pr

def F_it(n):
    if n < 2:
        return 1
    val = [1, 1]
    sign = 1  
    for i in range(2, n + 1):
        fm1 = val[i - 1] if i - 1 >= 0 else 0
        fm3 = val[i - 3] if i - 3 >= 0 else 0
        fn = math.factorial(i)
        fn2 = math.factorial(2 * i) 
        pr = sign * (2 * fm1 / fn + fm3 / fn2)
        val.append(pr)
        sign *= -1
    return val[n]

def compare_functions(n, repeats=1000):
    print("n         Рекурсивно (мс)     Итерационно (мс)")
    print("-" * 50)
    for n in range(1, n+1):
        rtime = timeit.timeit(lambda: F_rec(n), number=10) * 100  
        itime = timeit.timeit(lambda: F_it(n), number=10) * 100 
        
        print(f"{n}         {rtime:.6f}            {itime:.6f}")

num = int(input("Введите число для вычисления функций: "))
n_fact = math.factorial(num)
n2_fact = math.factorial(2 * num)
compare_functions(num)
answr = F_rec(num)
answit = F_it(num)
print(f"Рекурсивно: {answr}\nИтеративно: {answit}")