def f(a):
    if a==18:
        return 1
    if a>18:
        return 0
    return f(a+1)+f(a*2)+f(a*3)


print(f(1))