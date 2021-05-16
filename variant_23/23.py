def func (a,b):
    if a==b:
        return 1
    if a>b or a==14:
        return 0
    return func(a+1,b) + func(a+2,b) + func(a*2,b)


print(func(4,10)*func(10,12)*func(12,14))