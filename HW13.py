try:
    a = int(input('введите число a '))
    b = int(input('введите число b '))
    print(a/b)
except ValueError:
    print('вы ввели букву, введите цифры ')
except ZeroDivisionError:
    while b == 0:
        print('Деление на 0, повторите ввод ')
        try:
            a = int(input('введите число a '))
            b = int(input('введите число b '))
        except ValueError:
            print('вы ввели букву, введите цифры ')
    else:
        print(a/b)