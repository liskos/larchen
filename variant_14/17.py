k = 0
for i in range(246815,875621):
    if (i%10000//1000 + i%1000//100) < 50 and i//1000%5==i%1000%5:
        k+=1
print(k)