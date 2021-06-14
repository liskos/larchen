import sys
sys.stdin=open("24data/k7-0.txt")
s=input()
print(s)
print(s.count("C"))
for i in range(1, 1000):
    if "С"*i in s:
        print(i)