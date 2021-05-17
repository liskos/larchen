k = 5273
for i in range(1005, 147870+1):
    r = max(map(int, str(i)))-min(map(int, str(i)))
    if str(i).count("1")==0 and r < 4:
        k -= 1
        print(k, i)
print(k)