k = 0
for i in range(1056,7564):
    if (i%3==0 or i%11==0) and i%13!=0 and i%17!=0 and i%19!=0 and i%23!=0:
        k+=1
        print(i)
print(k)