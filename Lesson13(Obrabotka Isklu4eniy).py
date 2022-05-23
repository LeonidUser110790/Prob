# a = 100/0
# print(a)

#обработка ошибки(пропуск ошибки)
# try:
#     b = 1/0
# except ZeroDivisionError:
#     b = 0
# print(b)

#пропуск ошибок
# try:
#     a = 2 + '1'
# except:
#     print('Ошибка в коде')

#print(int('qwerty'))


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print("Ключа не существует")


# my_list = [1,2,3,4,5]
# try:
#     my_list[6]
# except IndexError:
#     print('Этого индекса нет в списке')


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['d']
# except(IndexError, KeyError):
#     print('Произошла ошибка IndexError или KeyError')


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['b']
# except KeyError:
#     print('Произошла ошибка KeyError')
# finally:
#     print('ошибок не произошло')


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['a']
# except KeyError:
#     print('Произошла ошибка KeyError')
# else:
#     print('ошибок не произошло')
# finally:
#     print('Я введусь в любом случае')


########################################   ПРАКТИКА   ###############################################

# try:
#     a = int(input('введите число a '))
#     b = int(input('введите число b '))
#     c = a/b
# except ZeroDivisionError:
#     print('Произошла неведомая ошибка')
# except ValueError:
#     print('Не то пальто')
# else:
#     print('результат в квадрате', c**2)
# finally:
#     print('конец')


