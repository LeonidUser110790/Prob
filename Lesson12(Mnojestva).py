# #создание
# num_set = {1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5}
# num_set.add(6)
# print(num_set)
# print(type(num_set))
#
# str_set = {'max', "Mix", 'Fallen'}
# print(str_set)
#
# mixed_set = {2.0, "Mix", (1, 2, 3, 2, 3, 2)}
# print(mixed_set)

# setmonth = {'jan', 'feb', 'mar', 'apr', 'may'}
# for i in setmonth:
#     print(i)

#добавление значения во множества(только однин элемент)
# setmonth = {'jan', 'feb', 'mar', 'apr', 'may'}
# setmonth.add(123)
# print(setmonth)

#удаление значения из множества(только один элемент)
# setmonth = {'jan', 'feb', 'mar', 'apr', 'may'}
# setmonth.discard('mar')
# setmonth.remove('apr')
# print(setmonth)

#удаление рандомного элемента, и присвоение его к переменной
# num_set = {1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5}
# a = num_set.pop()
# print(num_set, a)
# num_set.pop()
# print(num_set)

#обьединение множеств, 2 варианта
#вариант 1
# months_a = {'jan', 'feb', 'mar'}
# months_b = {'apr', 'may', 'june', 'jule', 'august'}
# all = months_a.union(months_b)
# print(all)
#вариант 2
# num_set = {1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5}
# num_set1 = {6,7,8,9}
# print(num_set|num_set1)

#удаление всего множества
# num_set = {1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5}
# num_set.clear()
# print(num_set)

#пересечение множеств(вывод повторяющихся значений в обоих множествах)
# num_set = {1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5}
# num_set1 = {6,7,8,9,2,3,4,5}
# inters = num_set.intersection(num_set1)
# print(inters)
# print(num_set.intersection(num_set1))
# print(num_set & num_set1)

#разница между множествами
# num_set = {1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5}
# num_set1 = {6,7,8,9,2,3,4,5}
# print(num_set - num_set1)
# print(num_set1 - num_set)

#метод множества
# num_set = {1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5}
# num_set1 = {6,7,8,9,2,3,4,5}
# print(num_set.isdisjoint(num_set1))
# num_set = {1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5}
# num_set1 = {6,7,8,9}
# print(num_set.isdisjoint(num_set1))

#длинна множества
# num_set = {1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 6}
# print(len(num_set))


#########################################      ПРАКТИКА     ####################################

# узнать есть ли дубликаты
# lst = {1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5}
# lst_set = set(lst)
# if len(lst) == len(lst_set):
#     print('дубликатов нет')
# else:
#     print('дубликаты есть')

#
# st = {'it', 'over', 'one'}
# froz = frozenset({1, 2, 'it', 'over', 'one'})

#выполнить обьединение и пересечение множеств
# slov = {'it', 'over', 'one'}
# frozen = frozenset({'english', 'lesson', 'one'})
# print(slov|frozen)
# print(slov.intersection(frozen))