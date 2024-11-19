import re
"""Целые четные числа. 
Заменять четные цифры, стоящие на нечетных местах словами 
(цифры от 0 до 9 на слова «ноль», «один», …, «девять»)."""
digit_to_word = {
    '0': 'ноль',
    '2': 'два',
    '4': 'четыре',
    '6': 'шесть',
    '8': 'восемь',
}

def process_without_non_numbers(text):
    filtered_text = re.sub(r'[^\d\s]', '', text)
    check = 1
    output = []
    for char in filtered_text:
        if char.isdigit():
            if int(char) % 2 == 0 and check % 2 == 0:
                output.append(digit_to_word[char])
            else:
                output.append(char)
            check += 1
        elif char == ' ':
            output.append(char)
            check += 1
    return ''.join(output)
while True:
    with open('Lab-4/input.txt', 'r') as f:
        text = f.read()
    processed_text = process_without_non_numbers(text)
    print(processed_text)
    break
