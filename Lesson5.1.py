i = 2
x = 1
while i < 125:
    if i % 2 == 0:
        x *= i
    i += 2
    print(x)
print(x)
