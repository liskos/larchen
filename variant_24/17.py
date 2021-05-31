k = 0
for i in range(-9563, -3102 + 1):
    if i % 7 == 0 and i % 11 != 0 and i % 23 != 0 and abs(i) % 10 != 8:
        k += 1
        print(i)
print(k)
