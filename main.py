
#напишите программу для бинарного поиска загаданного числа

def binary_search(min_num, max_num):
    # min_num = 0
    # max_num = 100
    center = (min_num + max_num) // 2

    while True:
        print(f'Ваше число {center}?')
        check = input('Если больше >, если меньше <, если равно =\n')

        if check == '>':
            min_num = center
            center = (min_num + max_num) // 2
        elif check == '<':
            max_num = center
            center = (min_num + max_num) // 2
        elif check == '=':
            print(f'Вы загадали {check}')
            break
        else:
            print('я не знаю это число')
        

binary_search(int(input('мин. число\n')), int(input('макс. число\n')))