def f(x):
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 7)
        x = x // 7
    return a,b

mas = []
for i in range(1,1000000):
    a, b = f(i)
    if a == 3 and b == 24:
        mas.append(i)
print(max(mas))
