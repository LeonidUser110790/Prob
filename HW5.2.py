import random

a = []
b = random.randint(1, 99)
c = random.randint(1, 99)
d = random.randint(1, 99)
e = random.randint(1, 99)
f = random.randint(1, 99)
g = random.randint(1, 99)
h = random.randint(1, 99)
a.append(b)
a.append(c)
a.append(d)
a.append(e)
a.append(g)
a.append(h)
a.append(f)
print(a)
k = 0
n = 0
for i in a:
    if i % 2 == 0:
        k += 1
    else:
        n += 1
m = 0
if k > n:
    for j in a:
        m += j
    print("сумма =", m)
else:
    print("произведение =", a[0]*a[2]*a[5])