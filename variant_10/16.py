def f(n):
    if n < 3:
        return n
    else:
        return f(n-1)+g(n-2)


def g(n):
    if n < 3:
        return  n+1
    else:
        return g(n-1)+f(n-2)


print(f(28))