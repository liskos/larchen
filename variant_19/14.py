x = 43*(7**103) -21*(7**57) + 98
s = ""
while x > 0:
    s = str(x % 7) + s
    x = x // 7
print(s)
print(s.count("6")*6+s.count("4")*4+2)