res = 0
try:
     while True:
        for numb in map(int, input('Введите числа: ').split()):
            res += numb
        print(f'{res} - для завершения введите не число')
except ValueError:
     print(res)