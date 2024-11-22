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
def check_num(n):
    transformed = False  
    result = '' 
    for i, char in enumerate(n):
        if char.isdigit(): 
            if int(char) % 2 == 0 and (i + 1) % 2 != 0:  
                result += digit_to_word[char]
                transformed = True
            else: result += char    
        else: result += char        
    return result, transformed
def split_alot(num_input):
    numbers = re.findall(r'\b\d+\b', num_input)  
    output = []
    for num in numbers:
        transformed_number, is_transformed = check_num(num)
        if is_transformed:  output.append(transformed_number)
    print(' '.join(output))  
while True:
    with open('Lab-4/input.txt', 'r') as f:
        num_input = f.read()
    split_alot(num_input)
    break
