"""Целые четные числа. 
Заменять четные цифры, стоящие на нечетных местах словами 
(цифры от 0 до 9 на слова «ноль», «один», …, «девять»)."""
import re

digit_to_word = {
    '0': 'ноль',
    '2': 'два',
    '4': 'четыре',
    '6': 'шесть',
    '8': 'восемь',
}
def transform_even_number(number):
    result = []
    i = 1
    for char in number:
        if char == '-':
            result.append(char)
            continue
        if i % 2 == 0 and char in digit_to_word:  
            result.append(digit_to_word[char])
        else:
            result.append(char)
        i+=1
    return ''.join(result)

def check_num(content):
 
    pattern = r'(?<!\S)-?\d+'
    matches = re.findall(pattern, content)  

    result = []

    for match in matches:
        number = int(match)  
        if number % 2 == 0:  
            transformed = transform_even_number(match)
            result.append(transformed)
    print(' '.join(result))

while True:
    with open('Lab-4/input.txt', 'r', encoding='utf-8') as f:
        num_input = f.read()
    check_num(num_input)
    break
