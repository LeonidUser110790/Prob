a = int(input("введите сторону треугольника 1 "))
b = int(input("введите сторону треугольника 2 "))
c = int(input("введите сторону треугольника 3 "))
if a+b>c and a+c>b and b+c>a:
    print("треугольник верный")
else:
    print("треуголник неверный")