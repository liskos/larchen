k=0
for i in range(1016,7937+1):
    a=i%10
    if (i%3==0) and i%7!=0 and i%17!=0 and i%19!=0 and i%27!=0:
        k+=1
        print(i)
print(k)