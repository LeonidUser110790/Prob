a = 0
while True:
    b = input()
    a += 1
    if b == "стоп" or b == "хватит" or b == "довольно":
        break
print("всего слов -", a)
