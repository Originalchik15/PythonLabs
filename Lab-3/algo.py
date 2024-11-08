digit_to_word = {
    '0': 'ноль',
    '2': 'два',
    '4': 'четыре',
    '6': 'шесть',
    '8': 'восемь',
}

def check_num(n, check):
    if n == ' ':
        return n,check + 1
    if eval(n) % 2 == 0 and check % 2 == 0:
        return digit_to_word[n],check + 1
    else:
        return n, check + 1

def split_alot(num_input):
    num_input.split()
    check = 1
    output = ''
    for num_part in num_input:
        flag, check = check_num(num_part, check)
        output += flag
    print(output)

while True:
    with open('Lab-3/input.txt','r') as f:
        num_input = f.read()
    split_alot(num_input) 
    break

