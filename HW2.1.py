print("определить високосный год")
a = int(input("введите год "))
if a%4==0 or a%400==0:
    print("год високосный")
elif a%100==0:
    print("год не високосный")
else:
    print("год не високосный")
