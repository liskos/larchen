k=0
l=0
for i in range(3672,9117+1):
    a=i%10
    if i%3==2 and i%5==4:
        k+=1
        l+=i
print(k,l)