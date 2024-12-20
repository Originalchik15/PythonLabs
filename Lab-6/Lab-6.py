import timeit
from itertools import permutations
'''. Пароль состоит из К символов. 
Первые Т символов – латинские буквы, остальные - латинские буквы или цифры. 
Обязательно наличие как минимум одной цифры. 
Все символы должны быть разные. Составьте все возможные пароли.'''
'''1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.
'''
#1 часть 
def var1(elements):
    def backtrack(path, rem, res):
        if not rem:
            res.append(path)
            return
        for i in range(len(rem)):
            backtrack(path + [rem[i]], rem[:i] + rem[i+1:], res)
    el = list(map(lambda e: e, elements))
    res = []
    backtrack([], el, res)
    return res

def var2(elements):
    el = list(map(lambda e: e, elements))
    return permutations(el,len(el))

K = int(input("Введите количество символов в пароле: "))
T = int(input("Введите количество первых символов которые должны быть буквами: "))
while True:
    password = str(input("Введите пароль: "))
    
    if len(password) == K and len(set(password)) == K and password[:T].isalpha() and any(d.isdigit() for d in password[T:]):
        print(f"Пароль '{password}' соответствует требованиям.")
        break
    else:
        print("Пароль не соответствует требованиям. Введите заново.")


tv1 = timeit.timeit("var1(password)", globals=globals(), number=1)
answ = var1(password)
for a in answ:
    for b in a:
        print(b, end='')
    print(end=' ')
print(f"\nВремя выполнения алгоритмически: {tv1:.6f} секунд")
tv2 = timeit.timeit("var2(password)", globals=globals(), number=1)
answ2 = var2(password)
for a in answ2:
    for b in a:
        print(b, end='')
    print(end=' ')
print(f"\nВремя выполнения функциями: {tv2:.6f} секунд")
