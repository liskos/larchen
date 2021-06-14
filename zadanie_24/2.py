import sys
sys.stdin=open("24data/k7-20.txt")
s=input()
c = "C"
while c in s:
     c += "C"
print(len(c) - 1)