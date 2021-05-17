def f(n):
    if n<=18:
        return n+3
    if n>18 and n%3==0:
        return (n//3)*f(n//3)+n-12
    return f(n-1)+n*n+5

def chet(x):
    while x > 0:
        if x % 2 != 0:
            return False
        x = x // 10
    return True

k=0
for n in range(1,1001):
    x = f(n)
    if chet(x):
        k+=1
print(k)