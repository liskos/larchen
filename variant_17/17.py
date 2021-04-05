x = []
for i in range(1032, 8415+1):
    if i //10 % 10 == 0:
        continue
    else:
        a = i % 100
        b = i // 100
        razn = abs(a-b)
        if razn > 70:
            x.append(i)
print(max(x), len(x))