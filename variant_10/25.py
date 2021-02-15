def fun(x):
    a = []
    for i in range(2, x):
        if x % i == 0:
            a.append(i)
    return a


for i in range(123, 1234+1, 2):
    mas = fun(i)
    if len(mas) == 4:
        print(mas)