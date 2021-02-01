def f(x):
    a = 0
    b = 1
    while x > 0:
        if x % 2 >0:
            a+=1
        else:
            b+= x % 5
        x = x // 5
    return a,b

mas = []
for i in range(1,1000000):
    a, b = f(i)
    if a == 2 and b == 9:
        mas.append(i)
print(min(mas))
print(max(mas))
print(len(mas))