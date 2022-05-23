import random
a = random.randint(1,10)
b = random.randint(1,2)
if b == 1:
    e = "красный"
else:
    e = "чёрный"
f = 5
while f > 0:
    c = int(input("введите число "))
    d = input("введите цвет ")
    if c == a and d == b:
        print("you win")
        break
    else:
        print("don't")
        print(f-1, "try left")
    f -= 1
if f == 0:
    print("you lose, right combination - ", a, e)
