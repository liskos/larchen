def f(a,b):
    if a==b:
        return 1
    if a>b or a==6:
        return 0
    return f(a+1,b)+f(a+2,b)+f(a+4,b)


print(f(2,13))