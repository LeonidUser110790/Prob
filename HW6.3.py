a = input("введите слово ")
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
print('количество уникальных букв в слове', len(b))