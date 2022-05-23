a = [1, 2, 3, 4, 5, 2, 4, 5, 6, 8, 2, 12, 3, 14, 12, 6, 12, 6, 2, 1]
b = []
for i in a:
    if a.count(i) > 2:
        b.append(i)
print(b)