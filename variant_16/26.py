import sys
file = open("Задание 26/26.txt")
sys.stdin = file

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(sum(a[:4]))