def f(n):
    if n <= 18:
        return n+3
    if n > 18 and n%3==0:
        return (n // 3) * f(n // 3) + n - 12
    else:
        return f(n-1) + n * n + 5


k=0
for i in range(1,1001):
    if i%2==0:
        k+=1
print(k)
