def kol_del(x):
    a = []
    for i in range(1, x+1):
        if x % i == 0:
            a.append(i)
    return a


max_k_del = 0
x = 0
for i in range(541, 1234+1):
    kol = kol_del(i)
    if len(kol) > max_k_del:
        x = i
        max_k_del = len(kol)
print(max_k_del, x)