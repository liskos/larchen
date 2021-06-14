import sys
sys.stdin=open("24data/k7a-1.txt")
s = input()
max_len = 0
t_l = 0
for c in s:
    if c in "ABC":
        t_l += 1
    else:
        t_l = 0
    max_len = max(max_len, t_l)
print(max_len)