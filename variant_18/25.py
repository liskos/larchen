def kol_del(x):
    k = 0
    for i in range(1, x+1):
        if x % i == 0:
            k+=1
    return k


m = 0
for x in range(541, 1234+1):
    if kol_del(x) == 32:
        print(x, kol_del(x))
