def f(a,b):
    if a==b:
        return 1
    if a>b:
        return 0
    if a // 10 < 9:
        return f(a+10,b)+f(a+1,b)
    return f(a+1,b)


print(f(11,27))