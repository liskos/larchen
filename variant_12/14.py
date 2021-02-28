x = 4**14 + 64**16 - 81
s = ""
while x > 0:
    s = str(x % 4) + s
    x = x // 6
print(s.count("3"))