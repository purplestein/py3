def my_dif(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        return


print(my_dif(int(input('Введите х: ')), int(input('Введите y: '))))
