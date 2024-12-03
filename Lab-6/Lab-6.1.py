import timeit
from itertools import permutations
'''. Пароль состоит из К символов. 
Первые Т символов – латинские буквы, остальные - латинские буквы или цифры. 
Обязательно наличие как минимум одной цифры. 
Все символы должны быть разные. Составьте все возможные пароли.'''
'''1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.

Ограничение на длину пароля l и вычисление суммы цифр в пароле
'''
def var1h(elements, l):
    def backtrack(path, rem, res):
        if len(path) > l:
            return
        if len(path) == l:
            res.append(path)
            return
        for i in range(len(rem)):
            backtrack(path + [rem[i]], rem[:i] + rem[i+1:], res)
    el = list(map(lambda e: e, elements))
    res = []
    backtrack([], el, res)
    return res

def var2h(elements, l):
    el = list(map(lambda e: e, elements))
    return list(permutations(el, l))

def sm(perm):
    return sum(int(d) for d in perm if d.isdigit())

K = int(input("Введите количество символов в пароле: "))
T = int(input("Введите количество первых символов которые должны быть точно буквами: "))
l = int(input("Введите длину пароля: "))
if l > K:
    print("Длина пароля не может быть больше количества символов")
    exit()
while True:
    password = str(input("Введите пароль: "))
    
    if len(password) == K and len(set(password)) == K and password[:T].isalpha() and any(d.isdigit() for d in password[T:]):
        print(f"Пароль '{password}' соответствует требованиям.")
        break
    else:
        print("Пароль не соответствует требованиям. Введите заново.")
    
tv1h = timeit.timeit(lambda: var1h(password, l), number=1)
answ_h = var1h(password, l)

for a in answ_h:
    print(''.join(a), end=' ')
print(f"\nВремя выполнения алгоритмически: {tv1h:.6f} секунд")


tv2h = timeit.timeit(lambda: var2h(password, l), number=1)
answ2_h = var2h(password, l)

for a in answ2_h:
    print(''.join(a), end=' ')
print(f"\nВремя выполнения функциями: {tv2h:.6f} секунд")

if answ_h:
    opt1 = max(answ_h, key=sm)
    print(f"Оптимальная перестановка var1h: {''.join(opt1)} с суммой {sm(opt1)}")
else:
    print("Нет доступных перестановок для var1h.")

if answ2_h:
    opt2 = max(answ2_h, key=sm)
    print(f"Оптимальная перестановка var2h: {''.join(opt2)} с суммой {sm(opt2)}")
else:
    print("Нет доступных перестановок для var2h.")