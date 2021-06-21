import sys
sys.stdin=open("Задание 24/24.txt")
s=input()
k1 = s.count("X"*10)
k2 = s.count("Y"*7)
k3 = s.count("Z"*5)

print(k1+k2+k3)