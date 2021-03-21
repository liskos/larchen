x = 5 * 7**3 + 2 * 5**2 + 3 * 5**3 * 7
s = ""
while x > 0:
    s = str(x % 7) + s
    x = x // 7
print(s.count("7"))