x = int(input('Введите значение x:'))
y = int(input('Введите значение y:'))
def my_func(x, y):
    x = x ** y
    return x

print(my_func(x, y))


x = int(input('Введите значение x:'))
y = int(input('Введите значение y:'))
def my_func_1(x,y):
    if x == 0: return 0
    if y < 0:
        x = 1.0/x
        y = -y
    res = 1
    while y > 0:
        res = res * x
        y = y-1
    return res

print(my_func_1(x, y))