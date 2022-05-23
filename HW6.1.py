a = int(input("введите число "))
b = []
for i in range(a+1):
    if i % 2 != 0:
        b.append(i)
print(b)