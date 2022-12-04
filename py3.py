def my_func():
    numb_1 = int(input('Введите первое число:'))
    numb_2 = int(input('Введите второе число:'))
    numb_3 = int(input('Введите третье число:'))
    return numb_1 + numb_2, numb_2 + numb_3, numb_3 + numb_1
print(max(my_func()))