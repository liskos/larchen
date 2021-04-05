def func(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return func(a+2,b) + func(a+3, b) + func(a*10+1,b)


print(func(3, 12) * func(12, 25))