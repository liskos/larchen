def f(a,b):
    if a==b:
        return 1
    if a>b:
        return 0
    return f(a+3,b)+f(a+1,b)


print(f(7,20))