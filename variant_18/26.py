import sys
file = open('Задание 26/26.txt')

sys.stdin = file
n = int(input())
mas = []
for i in range(n):
    mas.append(int(input()))
print(mas)
mas.sort()
print(mas)
print(sum(mas[:10]))