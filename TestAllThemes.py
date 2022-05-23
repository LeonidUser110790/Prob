#ВВод Вывод Типы Данных

# a = 199
# print(a)
# b = input('введите число ')
# num2 = int(b)
# print(b)
# c = a-num2
# print(c)
# d = a*num2
# print(d)
# e = a/num2
# print(e)
# f = a%num2
# print(f)
# g = c+d+e+f
# print(g)

# num1 = 22
# num2 = 31
# num3 = 43
# print(num1+num2+num3)

# kat1 = int(input('введите катет 1: '))
# kat2 = int(input('введите катет 2: '))
# a = kat1*kat2
# print(a)
# s = a/2
# print('площадь треугольника равна', s)

# name = input('введите своё имя ')
# print('Hello', name, '!!!')

# n = int(input('введите количество школьников '))
# k = int(input('введите количество яблок '))
# num1 = k//n
# num2 = k%n
# print(num1, 'яблок достанется каждому школьнику')
# print(num2, 'яблок останется в корзине')


# num1 = int(input('введите целое число '))
# if num1 >0:
#     print(num1+1)
# else:
#     print(num1)

# num1 = int(input('введите число '))
# if num1%2==0:
#     print('число чётное')
# else:
#     print('число нечётное')

# num1 = int(input('введите число '))
# num2 = int(input('введите число '))
# num3 = int(input('введите число '))
# if num1<num2 and num1<num3:
#     print(num1, 'наименьшее из 3-х чисел')
# elif num2<num1 and num2<num3:
#     print(num2, 'наименьшее из 3-х чисел')
# else:
#     print(num3, 'наименьшее из 3-х чисел')

# age = int(input('введите свой возраст '))
# if age<7:
#     print('вы дошкольник')
# elif age<18:
#     print('вы школьник')
# elif age<27 and age>28:
#     print('вы работник')
# elif age==28:
#     print('Светик, вы замечательный человек, вам не нужно работать')
# else:
#     print('вы пенсионер')

# num1 = int(input('введите число '))
# if num1==11:
#     print('угадал')
# elif num1<0:
#     print('Не в ту сторону считаешь')
# elif num1>31:
#     print('В месяце не может быть больше 31 дня')
# else:
#     print('всё по пизде')

# num1 = int(input('введите число 1: '))
# num2 = int(input('введите число 2: '))
# a = input('введите знак выражения ')
# if a == '+':
#     print(num1+num2)
# elif a == '-':
#     print(num1-num2)
# elif a == '*':
#     print(num1*num2)
# elif a == '/':
#     print(num1/num2)
# elif a == '/' and num2 == 0:
#     print('делить на ноль нельзя')
# else:
#     print('неверно введены данные')

# num1 = int(input('введите двузначное число '))
# num2 = num1//10
# num3 = num1%10
# print(num2)
# print(num3)
# sum = num2+num3
# print(sum)

# storona1 = int(input('введите сторону треугольника а: '))
# storona2 = int(input('введите сторону треугольника b: '))
# storona3 = int(input('введите сторону треугольника c: '))
# if storona3+storona2>=storona1 and storona3+storona1>=storona2 and storona1+storona2>=storona3:
#     print('треугольник существует')
# else:
#     print('треугольник не существует')

# num1 = int(input('введите трёхзначное число '))
# num1_1 = num1%100
# num2 = num1//100
# num3 = num1_1//10
# num4 = num1_1%10
# sum = num2+num3+num4
# print(sum)
# if num1%2==0:
#     print(sum)
# else:
#     print(num2*num3*num4)

# x = int(input('введите координату x: '))
# y = int(input('введите координату y: '))
# if x>0 and y>0:
#     print('точка принадлежит первой четверти')
# elif x<0 and y>0:
#     print('точка принадлежит второй четверти')
# elif x<0 and y<0:
#     print('точка принадлежит трейтей четверти')
# elif x>0 and y<0:
#     print('точка принадлежит четвёртой четверти')

#############################     строки

# word = input('введите слово ')
# print(word[2])
# print(word[-2])
# print(word[0:5])
# print(word[0:-2])
# print(word[0::2])
# print(word[1::2])
# print(word[::-1])
# print(word[::-2])
# print(len(word))

# word = input('введите фразу ')
# if word[0::1] == word[-1::-1]:
#     print('Pallindrom')
# else:
#     print('tufta')     #Как сделать программу не чувствительной к регистру??


#################################  Цикл for

#Написать программу, которая выводит числа от 0 до 100 на экран, пропуская числа кратные 7
# for i in range(0, 101):
#     if i%7==0:
#         continue
#     print(i, end=' ')

#Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
# a = 0
# for i in range(0, 101):
#     a += i
# print(a)

# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
# По данному натуральному n вычислите значение n!.
# Пользоваться математической библиотекой math в этой задаче запрещено.
# a = 1
# b = int(input('enter the number '))
# for i in range(1, b + 1):
#     a *= i
# print(a)

#Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
#Подсчитайте количество нулей среди введенных чисел и выведите это количество.
#Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
#Сделайте так же, как в примере работы программы.
# num_zeroes = 0
# # for i in range(int(input('сколько чисел вводим? '))):
# #     if int(input('введите число ')) == 0:
# #         num_zeroes += 1
# # print(num_zeroes)

# Пользователь передает целое положительное число N,
# выведете на экран последовательность от 1 до N "ёлочкой", например для N=17:
#net resheniya


################################  цикл while

#Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
# num = int(input('введите целое число, не меньше 2 '))
# a = 1
# while a<num:
#     a += 1
#     if num%a==0:
#         print(a)
#         break

#Выведите все квадраты натуральных чисел, не превосходящие данного числа N.
# num = int(input('введите целое число '))
# a = 1
# while a**2<num:
#     print(a**2, end=' ')
#     a+=1

#Дано целое число. Проверить и вывести, является ли это число простым.
# num = int(input('введите целое число '))
# a = 2
# while num%a!=0:
#     a+=1
#     if a==num:
#         print('число простое')
#         break
# else:
#     print('число не простое')

#Распечатать таблицу умножения от 1 до 9 на числа от 1 до 10.
# for i in range(1,10):
#     for j in range(1, 11):
#         print(i,'*',j,'=',(i*j))
#     print()

