a = []
for i in range(246815, 875621+1):
    s = str(i)
    if int(s[-4]+s[-3])<50 and (i % 1000 % 5 == i //1000 %5):
        a.append(i)
print(max(a), len(a))