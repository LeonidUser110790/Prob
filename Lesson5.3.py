a = float(input("введите число 1 "))
b = float(input("введите число 2 "))
c = input("введите знак ")
while True:
    if c == "+":
        d = a+b
    elif c == "-":
        d = a-b
    elif c == "*":
        d = a*b
    elif c == "/":
        if b == 0:
            print("на ноль нельзя делить")
        else:
            d = a/b
    print(a, c, b, "=", d)
    break
