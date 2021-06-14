import sys
sys.stdin=open("Задание 24/24.txt")
s=input()
k1 = s.count("ZYX")
k2 = s.count("XYZ")
k3 = s.count("XYZYX")

print(k1+k2 - k3)