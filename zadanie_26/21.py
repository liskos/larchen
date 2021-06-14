import sys
sys.stdin = open(file="26data/26-k1.txt")

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)

print("цену самого дорогого товара, не участвующего в распродаже", a[k])
print("целую часть от суммы всех скидок", int(sum(a[:k])*0.2))
