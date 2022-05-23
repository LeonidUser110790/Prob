# print("I", "like", "python", sep="***")

# name = input("ввести имя ")
# print("Привет", name, sep=", ", end="!")

# num = int(input("введите число "))
# print("следующее число ", num + 1)
# print("предидущее число ", num -1)

# password = input("введите пароль ")
# password_indif = input("подтвердите пароль ")
# if password == password_indif:
#     print('пароль верный')
# else:
#     print("пароль неверный")

# num = int(input("введите четырёхзначное число "))
# if 999 < num < 9999:
#     if num % 77 == 0 or num % 1717 == 0:
#         print("Yes")
#     else:
#         print("No")
# else:
#     print("ввели неверное число")

# age = int(input("введите возраст "))
# pol = input("введите пол ")
# if 9 < age < 16 and pol == "f":
#     print("Yes")
# else:
#     print("No")

# a = input("введите основной цвет ")
# b = input("с чем смешиваем ")

# if a == "красный":
#     if a == b:
#         print("красный")
#     elif b == "синий":
#         print("фиолетовый")
#     elif b == "желтый":
#         print("оранжевый")
#     else:
#         print("ошибка цвета")
# elif a == "синий":
#     if a == b:
#         print("синий")
#     elif b == "красный":
#         print("фиолетовый")
#     elif b == "желтый":
#         print("зеленый")
#     else:
#         print("ошибка цвета")
# elif a == "желтый":
#     if a == b:
#         print("желтый")
#     elif b == "синий":
#         print("зеленый")
#     elif b == "красный":
#         print("оранжевый")
#     else:
#         print("ошибка цвета")
# else:
#     print("ошибка цвета")

# a = input("введите название первого города ")
# b = input("введите название второго города ")
# c = input("введите название третьего города ")
# a1 = min(len(a), len(b), len(c))
# a2 = max(len(a), len(b), len(c))
#
# if a1 == len(a):
#     print(a)
# elif a1 == len(b):
#     print(b)
# else:
#     print(c)
# if a2 == len(a):
#     print(a)
# elif a2 == len(b):
#     print(b)
# else:
#     print(c)

# a = input("введите строку ")
# if "синий" in a:
#     print("Yes")
# else:
#     print("No")

# num = int(input("длина катета треугольника "))
# b = input("символ ")
#
# for i in range(num):
#     print(b*(num-i))

#таблица умножения
# a = int(input("введите число "))
# for i in range(1, 10):
#     print(a, "*", i, "=", a*i)

#последовательность  Фибоначчи:
# n = int(input("введите число "))
# a, b = 1, 1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

# n = int(input('Введите число натуральное: '))
# total = 0
# summ = 0
# proizv = 1
# last = n % 10
# while n != 0:
#     last_digit = n % 10
#     total += 1
#     summ += last_digit
#     proizv *= last_digit
#     sr = summ / total
#     l = last + last_digit
#     n = n // 10
# print(n, total, summ, proizv, last, l, sep="\n")