def my_dif():
    try:
        numb_1 = int(input('Введите первое число:' ))
        numb_2 = int(input('Введите второе число:' ))
        res = numb_1 / numb_2   
        return res
    except ZeroDivisionError:
        return 
print(my_dif())
