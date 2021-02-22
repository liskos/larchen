x = 36**27 + 6 ** 18 -19
s = ""
while x > 0:
    s = str(x % 6) + s
    x = x // 6
print(s)
print(s.count("0"))