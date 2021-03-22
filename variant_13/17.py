a = []
for i in range(12345, 54321+1):
    s = str(i)
    if (i %3 ==2) and (i %7 ==6) and (i %9 ==8) and s[0] != s[-1]:
        a.append(i)
print(max(a), len(a))