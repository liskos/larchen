x = (24399*42202)
s = ""
while x > 0:
    s = str(x % 2) + s
    x = x // 2
print(s)
print(s.count("1"))