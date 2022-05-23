# with open('text.txt', mode='r', encoding='utf-8') as file:
#     text = file.read().split('\n')
#     print(text, type(text))


# with open('text.txt', mode='w', encoding='utf-8') as file:
#     text = file.writelines(['хорошего дня\n', 'bye\n'])
#     print(text, type(text))

# with open('text.txt', mode='a', encoding='utf-8') as file:
#     text = file.write('bye\n')
#     print(text, type(text))


# Пользователь - продавец магазина.
# Вам нужно написать программу, которая будет спрашивать у пользователя,
# какие товары имеются в магазине то тех пор,
# пока пользователь не вводит пустую строчку.
# Каждый товар пишется в отдельную строку в файле shop.txt.
# Итоговый файл выглядит следующим образом:
# with open('shop.txt', mode='a', encoding='utf-8') as file:
#     while True:
#         a = input('Введите товар: ')
#         if a == ' ':
#             break
#         file.write(a+'\n')


#открытие файлы с любого места компа
# with open('C:/Users/Лёня Невопрос/Desktop/Новый текстовый документ.txt', mode='a', encoding='utf-8') as file:
#     while True:
#         a = input('Введите товар: ')
#         if a == ' ':
#             break
#         file.write(a+'\n')


import os
#
# name = os.getcwd()
# print(name)
# os.chdir('..')
# name = os.getcwd()
# print(name)
# os.chdir('Prob')
# name = os.getcwd()
# print(name)


# os.mkdir('test2')
# os.chdir('test2')
# name = os.getcwd()
# print(name)
# with open('test.txt', mode='w', encoding='utf-8') as file:
#     file.write('hey')

l = os.listdir()
print(l)

os.removedirs('test2')