k=0
for i in range(4563,7913):
    a=i%10
    b=i//1000
    if i%7==0 and a+b>10:
        k+=1
print(k)
