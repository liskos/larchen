k=0
for i in range(-9563,-3102+1):
    a=i%10
    if i%7==0 and i%11!=0 and i%23!=0 and a!=8:
        k+=1
        print(i)
print(k)
