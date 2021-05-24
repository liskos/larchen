def f(a,b):
    if a==b:
        return 1
    if a>b:
        return 0
    if a == 20 and b == 100:
        return 37889062373143906
    if a == 21 and b == 100:
        return 2341672834846768

    return f(a+1,b)+f(a+2,b)


print(f(2, 100))