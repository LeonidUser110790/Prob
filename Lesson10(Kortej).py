# a = ("a", "12", [1, 3, 2], "1.22")
# # print(a[2][1])
# # a[2].append(33)
# # print(a)
# # a[2][1] = 21
# # print(a)
# # a[1] = 22
# # print(a)



# a = ("mon", "tue", 'when', 'thr', 'fri', 'sat', 'san')
# day = str(input("day is "))
# if day in a:
#     num = a.index(day)
#     print('number of day ', num+1)
# else:
#     print('wrong day')


import random
a = [random.randint(1,100) for i in range(10)]
a = tuple(a)
print(a)
print(a.index(min(a)),a.index(max(a)))
