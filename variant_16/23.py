def func(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    if b % 2 == 0:
        return func(a, b-1) + func(a, b//2)
    else:
        return func(a, b-1)


print(func(1, 10) * func(10, 21))
