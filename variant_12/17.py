k = 0
for i in range(1024,2049):
    if i % 7 == 0 and i % 11 != 0 and i % 19 != 0:
        k+=1
        print(i)
print(k)