k=0
for i in range(1170,8367+1):
    a=i%10
    if (i%3==0 or i%7==0) and i%11!=0 and i%13!=0 and i%17!=0 and i%19!=0:
        k+=1
        print(i)
print(k)