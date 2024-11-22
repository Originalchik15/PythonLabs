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
def check_num(n, check):
    transformed = False 
    result = ''  
    for char in n:
        if char.isdigit():
            if int(char) % 2 == 0 and check % 2 != 0:
                result += digit_to_word[char]
                transformed = True
            else:
                result += char
            check += 1
        else:
            result += char
            check += 1
    return result, transformed
def split_alot(num_input):
    num_input = num_input.split() 
    output = []
    for num_part in num_input:
        if num_part.lstrip('-').isdigit(): 
            is_negative = num_part[0] == '-'  
            num_body = num_part[1:] if is_negative else num_part
            transformed_number, is_transformed = check_num(num_body, 1)
            if is_transformed: 
                if is_negative:
                    transformed_number = '-' + transformed_number  
                output.append(transformed_number)
    
    print(' '.join(output)) 
while True:
    with open('Lab-3/input.txt', 'r', encoding='utf-8') as f:
        num_input = f.read()
    split_alot(num_input)
    break
