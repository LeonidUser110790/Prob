print("введите координаты и радиус круга")
x = float(input("x= "))
y = float(input("y= "))
r = float(input("r= "))
import math
hypot = math.sqrt(x**2 + y**2)
print(hypot)
if hypot <= r:
    print("точка принадлежит кругу")
else:
    print("точка не принадлежит кругу")